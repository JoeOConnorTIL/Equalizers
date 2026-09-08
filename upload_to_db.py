import duckdb
from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')
database='my_db'
schema='development'
endpoint='fixtures'
table_name='fixtures'

con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

# con.sql("SHOW DATABASES").show()
# con.sql(f"USE {database}")
# con.sql("SELECT current_database()").show()


target_dir = "./data"
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
                    con.execute(f"""
                        INSERT INTO {database}.{schema}.{folder.name}_raw
                        BY NAME
                        SELECT * FROM '{file_path.as_posix()}'
                            """)
        else:
            print('table does not yet exist, creating table')
            con.execute(f"""
                CREATE TABLE IF NOT EXISTS {database}.{schema}.{folder.name}_raw AS
                SELECT * FROM './data/{folder.name}/*.json'
                """
                        )


        # for file_path in folder.rglob("*.json"):
        #     if file_path.is_file():
        #         print(f"  File: {file_path}")



# con.execute(f"""
#     CREATE TABLE IF NOT EXISTS {database}.{schema}.{table_name}_raw AS
#     SELECT * FROM './data/{endpoint}/*.json'
# """
# )