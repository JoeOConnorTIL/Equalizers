import requests
import os
from dotenv import load_dotenv
import logging
import time

# Premier League is league # 39, Season is defined by the year it starts in i.e. 2026 for 2026/27

base_url = "https://v3.football.api-sports.io/"
new_matches = [1035037, 1035038, 1035039, 1035041]
logger=logging.getLogger()
load_dotenv()
FOOTBALL_API_KEY=os.getenv('FOOTBALL_API_KEY')

def extract_new_statistics(new_matches:list, max_retry=3):

  logger.info('Starting extraction for new fixtures statistics')

  payload={}
  headers = {
    'x-apisports-key': FOOTBALL_API_KEY,
  }

  data_dir= f'data/statistics'
  os.makedirs(data_dir, exist_ok=True)

  if len(new_matches) == 0:
    logger.info('No new matches have been completed, ending script')
    return

  for match in new_matches:

    attempt = 0
    delay = 6 

    while attempt <= max_retry:
      
        response = requests.request("GET", f'{base_url}fixtures/statistics?&fixture={match}', headers=headers, data=payload)

        status=response.status_code

        data = response.text

        filename = f"{data_dir}/test_statistics_{str(match)}.json"

        if status == 200:
                   
          try:
            with open(filename, "w") as f:
                f.write(data)
                time.sleep(6)
                break

          except Exception as e:
            logger.error(f'Error saving statistics for fixture {match}: {e}')
            break

        elif status == 204:
           errors=response.errors
           logger.error(f'Error: match id {match} - {errors}')
           break

        else:
          if attempt == max_retry:
             logger.info(f'Response status: {status} - Max retries exceeded - inspect error.')
             break
          else:
            logger.info(f'Response status: {status} - attempt {attempt}, retrying.')
            attempt += 1
            time.sleep(delay*attempt)


        
extract_new_statistics(new_matches, 3)