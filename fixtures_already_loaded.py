import duckdb
from dotenv import load_dotenv
import os
import pandas

load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')
database='my_db'
schema='development'
endpoint='fixtures'
table_name='fixtures'

con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

fixture_ids= (
    con.execute(f"""select unnest(response)['fixture']['id'] as id from {schema}.fixtures_raw""")
    .df()['id']
    .tolist()
)

print (fixture_ids)
print (len(fixture_ids))