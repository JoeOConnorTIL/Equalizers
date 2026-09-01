import duckdb
from dotenv import load_dotenv
import os
from game_ids_already_loaded import game_ids_already_loaded
import logging
from datetime import datetime, timedelta, timezone
from logger import initiate_log
import requests
from matches_completed import matches_completed
from fetch_new_fixtures import extract_new_fixtures

# Setting variables
load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')
FOOTBALL_API_KEY=os.getenv('FOOTBALL_API_KEY')
base_url = "https://v3.football.api-sports.io/"
endpoint= "fixtures"
league_id= '39'
season = '2023'
status = 'FT'
database='my_db'
schema='development'
endpoint='fixtures'
table_name='fixtures'
log_dir='ingestion_logs'
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # gives the date/time now

# Initiating logger
logger = initiate_log(timestamp, log_dir, 'equalizers')
logger.info('Logger Successfully Initiated')

# Listing Fixtures already loaded to database
A = game_ids_already_loaded(schema, endpoint)
# Listing all completed fixtures this season
B = matches_completed(season, status, league_id, endpoint)
# Fixtures which are completed but not in our database yet
new_games= list(set(B) - set(A))

extract_new_fixtures(new_games, 4)

# print (A)
# print (B)
# print (new_games)