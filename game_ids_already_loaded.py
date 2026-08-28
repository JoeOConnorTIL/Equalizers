import duckdb
from dotenv import load_dotenv
import os
import logging

load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')
database='my_db'
schema='development'
endpoint='fixtures'
table_name='fixtures'
logger=logging.getLogger()

def game_ids_already_loaded(schema='development', endpoint='fixtures'):

    """
    Returns a list of the game id's already loaded into the raw table within your schema. The naming convention for the raw tables is endpoint_raw. This function defaults to the 'fixtures' endpoint and the 'development' schema and therefore the fixtures_raw table within development. This function also requires that you define a valid motherduck_token before calling the function.
    """

    con = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

    try:

        fixture_ids= (
            con.execute(f"""select unnest(response)['fixture']['id'] as id from {schema}.{endpoint}_raw""")
            .df()['id']
            .tolist()
        )
        logger.info('Existing fixture ids fetched')

        return(fixture_ids)
    
    except Exception as  e: 
        logger.error(f'An error occurred: {e}')