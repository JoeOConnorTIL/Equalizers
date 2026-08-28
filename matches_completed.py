import requests
import os
from dotenv import load_dotenv
import logging


# Premier League is league # 39, Season is defined by the year it starts in i.e. 2026 for 2026/27

base_url = "https://v3.football.api-sports.io/"
endpoint= "fixtures"
league_id= '39'
season = '2023'
status = 'FT'

load_dotenv()
FOOTBALL_API_KEY=os.getenv('FOOTBALL_API_KEY')
logger = logging.getLogger()

def matches_completed(season:int, status='FT', league_id='39', endpoint='fixtures'):

    """
    Calls the fixtures API as standard, and returns a list of all game ids which have the status of 'FT' indicating that the match has been completed. Standard input for league id is 39 for the premier league, and endpoint is fixtures. Season is defined as the year in which the season started i.e. for 2026/27 this season would be returned from inputting 2026.
    """

    payload={}
    headers = {
    'x-apisports-key': FOOTBALL_API_KEY,
    }

    try:

        response = requests.request("GET", f'{base_url}{endpoint}?league={league_id}&season={season}&status={status}', headers=headers, data=payload)

        data = response.json()

        match_ids = match_ids = [item['fixture']['id'] for item in data['response']]
        logger.info('Successfully fetched completed matches')

        return(match_ids)

    except Exception as e:
        logger.error(f'Error retrieving completed matches from API: {e}')