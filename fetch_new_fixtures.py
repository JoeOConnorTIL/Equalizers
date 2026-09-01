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
new_matches = [1035037, 1035038, 1035039, 1035041]
logger=logging.getLogger()


load_dotenv()
FOOTBALL_API_KEY=os.getenv('FOOTBALL_API_KEY')

def extract_new_fixtures(new_matches:list):

  payload={}
  headers = {
    'x-apisports-key': FOOTBALL_API_KEY,
  }

  if len(new_matches) == 0:
    logger.info('No new matches have been completed, ending script')
    return

  for match in new_matches:
    
    response = requests.request("GET", f'{base_url}fixtures?&id={match}', headers=headers, data=payload)

    data = response.text

    data_dir= f'data/fixtures'
    os.makedirs(data_dir, exist_ok=True)
    filename = f"{data_dir}/test_fixtures_{str(match)}.json"

    with open(filename, "w") as f:
        f.write(data)


extract_new_fixtures(new_matches)