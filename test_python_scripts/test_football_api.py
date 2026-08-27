import requests
import os
from dotenv import load_dotenv

base_url = "https://v3.football.api-sports.io/"
endpoint= "leagues"
load_dotenv()
FOOTBALL_API_KEY=os.getenv('FOOTBALL_API_KEY')

payload={}
headers = {
  'x-apisports-key': FOOTBALL_API_KEY,
}

response = requests.request("GET", f'{base_url}{endpoint}', headers=headers, data=payload)

data = response.text

data_dir= 'sample_data'
os.makedirs(data_dir, exist_ok=True)
filename = f"{data_dir}/test_{endpoint}.json"

with open(filename, "w") as f:
    f.write(data)