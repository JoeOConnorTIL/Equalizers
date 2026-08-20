from google import genai
from dotenv import load_dotenv
import os
import json


load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client()

dataset_json = {
    "users": [
        {"id": 1, "signup_days_ago": 120, "sessions": 45, "converted": True, "spend": 120.50},
        {"id": 2, "signup_days_ago": 10,  "sessions": 2,  "converted": False, "spend": 0.00},
        {"id": 3, "signup_days_ago": 300, "sessions": 12, "converted": True, "spend": 450.00},
        {"id": 4, "signup_days_ago": 45,  "sessions": 88, "converted": False, "spend": 0.00}
    ]
}

prompt= f""" Analyze the dataset provided below. Identify interesting patterns, anomalies, or statistical observations, 
and generate a list of insightful statistical questions based on those findings.

Dataset:
{json.dumps(dataset_json)}
"""
# Using Interactions

interaction = client.interactions.create(
    model="gemini-3.5-flash-lite",
    input=prompt
)

print(interaction.output_text)