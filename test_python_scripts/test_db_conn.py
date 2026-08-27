import duckdb
from dotenv import load_dotenv
import os

load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')

con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

con.sql("SHOW DATABASES").show()
con.sql("USE my_db")
con.sql("SELECT current_database()").show()

con.execute("""
    CREATE TABLE IF NOT EXISTS my_db.test_upload AS
    SELECT * FROM './sample_data/test.json'
"""
)