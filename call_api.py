import requests
import os
from dotenv import load_dotenv

# Premier League is league # 39, Season is defined by the year it starts in i.e. 2026 for 2026/27

base_url = "https://v3.football.api-sports.io/"
endpoint= "fixtures"
league_id= '39'
season = '2026'

load_dotenv()
FOOTBALL_API_KEY=os.getenv('FOOTBALL_API_KEY')

payload={}
headers = {
  'x-apisports-key': FOOTBALL_API_KEY,
}

response = requests.request("GET", f'{base_url}{endpoint}?league={league_id}&season={season}', headers=headers, data=payload)

data = response.text

data_dir= f'data/{endpoint}'
os.makedirs(data_dir, exist_ok=True)
filename = f"{data_dir}/test_{endpoint}_{league_id}_{season}.json"

with open(filename, "w") as f:
    f.write(data)