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
            table_exists = bool(
                con.sql(f"""
                SELECT 1 
                FROM information_schema.tables 
                WHERE table_catalog = '{database}' 
                AND table_schema = '{schema}' 
                AND table_name = '{raw_table}'
                """).fetchone()
            )
            logger.info(f"Table: {table_name}")
            logger.info(f'Table Exists?: {table_exists}')
            if table_exists:
                logger.info('table exists, uploading files')
                # Upload data to table
                for file_path in folder.rglob("*.json"):
                    if file_path.is_file():
                        logger.info(f" Working through file: {file_path}")
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
                logger.info('table does not yet exist, creating table')
                try:
                    con.execute(f"""
                    CREATE TABLE IF NOT EXISTS {database}.{schema}.{folder.name}_raw AS
                    SELECT * FROM './data/{folder.name}/*.json'
                    """
                            )
                    os.remove(folder)
                except Exception as e:
                    logger.error(f'Error creating table: {e}')
