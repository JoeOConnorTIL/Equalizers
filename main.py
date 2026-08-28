import duckdb
from dotenv import load_dotenv
import os
from game_ids_already_loaded import game_ids_already_loaded
import logging
from datetime import datetime, timedelta, timezone
from logger import initiate_log

# Setting variables
load_dotenv()
motherduck_token= os.getenv('DBT_ENV_SECRET_MOTHERDUCK_TOKEN')
database='my_db'
schema='development'
endpoint='fixtures'
table_name='fixtures'
log_dir='ingestion_logs'
timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S') # gives the date/time now

# Initiating logger
logger = initiate_log(timestamp, log_dir, 'equalizers')
logger.info('Logger Successfully Initiated')

A = game_ids_already_loaded(schema, endpoint)