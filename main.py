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
from fetch_new_statistics import extract_new_statistics

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
A = game_ids_already_loaded(schema, 'fixtures')
# Listing all completed fixtures this season
B = matches_completed(season, status, league_id, 'fixtures')
# Fixtures which are completed but not in our database yet
## Commented out for testing ## new_fixtures= list(set(B) - set(A))
new_fixtures= [1035137, 1035138, 1035139, 1035140, 1035141, 1035142, 1035143, 1035144, 1035145, 1035146, 1035147, 1035148, 1035149, 1035150, 1035151, 1035152, 1035153, 1035154, 1035155, 1035156]

# Extracting fixtures
extract_new_fixtures(new_fixtures, 4)

C = game_ids_already_loaded(schema, 'statistics')

## Commented out for testing ##  new_statistics= list(set(B) - set(C))
new_statistics= [1035137, 1035138, 1035139, 1035140, 1035141, 1035142, 1035143, 1035144, 1035145, 1035146, 1035147, 1035148, 1035149, 1035150, 1035151, 1035152, 1035153, 1035154, 1035155, 1035156]

# Extracting Statistics
extract_new_statistics(new_statistics, 4)

# Testing that lists are working correctly
# print('List A')
# print (A)
# print('List B')
# print (B)
# print('new_fixtures')
# print (new_fixtures)
# print('List C')
# print (C)
# print('new_statistics')
# print(new_statistics)