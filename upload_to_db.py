import duckdb
from dotenv import load_dotenv
import os
from pathlib import Path
from logging import getLogger

logger =getLogger()
load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')

def upload_to_db(target_dir = "./data", database = 'my_db', schema = 'development'):

    con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')
    base_path = Path(target_dir)

    for folder in base_path.iterdir():
        raw_table=f'{folder.name}_raw'
        if folder.is_dir():
            table_name = f"{database}.{schema}.{folder.name}_raw"
            print(f"Table: {table_name}")
            table_exists = bool(
                con.sql(f"""
                SELECT 1 
                FROM information_schema.tables 
                WHERE table_catalog = '{database}' 
                AND table_schema = '{schema}' 
                AND table_name = '{raw_table}'
                """).fetchone()
            )
            print(f"Table: {table_name}")
            print(f'Table Exists?: {table_exists}')
            if table_exists:
                print('table exists, uploading files')
                # Upload data to table
                for file_path in folder.rglob("*.json"):
                    if file_path.is_file():
                        print(f"  File: {file_path}")
                        try:
                            con.execute(f"""
                            INSERT INTO {database}.{schema}.{folder.name}_raw
                            BY NAME
                            SELECT * FROM '{file_path.as_posix()}'
                                """)
                            logger.info(f'{file_path} loaded to {database}.{schema}.{folder.name}_raw')
                            os.remove(file_path)
                        except Exception as e:
                            logger.error(f'Error loading {file_path} to database: {e}')
            else:
                print('table does not yet exist, creating table')
                try:
                    con.execute(f"""
                    CREATE TABLE IF NOT EXISTS {database}.{schema}.{folder.name}_raw AS
                    SELECT * FROM './data/{folder.name}/*.json'
                    """
                            )
                    os.remove(folder)
                except Exception as e:
                    logger.error(f'Error creating table: {e}')
                    print(f'Error creating table: {e}')
