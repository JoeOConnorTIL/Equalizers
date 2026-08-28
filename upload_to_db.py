import duckdb
from dotenv import load_dotenv
import os

load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')
database='my_db'
schema='development'
endpoint='fixtures'
table_name='fixtures'
filename='test_fixtures_39_2024'

con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

con.sql("SHOW DATABASES").show()
con.sql(f"USE {database}")
con.sql("SELECT current_database()").show()

con.execute(f"""
    CREATE TABLE IF NOT EXISTS {database}.{schema}.{table_name}_raw AS
    SELECT * FROM './data/{endpoint}/*.json'
"""
)