import requests
import os
import json
from dotenv import load_dotenv 

load_dotenv()

API_URL = "https://data.usajobs.gov/api/search"
HOST = "data.usajobs.gov"
USER_AGENT = os.environ.get("USER_AGENT") #Load from variables 
AUTH_KEY = os.environ.get("AUTH_KEY") #Load from variables 

def fetch_jobs():
  headers = {
    "Host": HOST,
    "User-Agent": USER_AGENT,
    "Authorization-key": AUTH_KEY
  }
  params = {
    "JobCategoryCode": "2210",
    "Keyword": "Remote"
  }
  response = requests.get(API_URL, headers=headers, params=params)
  if response.status_code == 200:
    data = response.json()
    print("API response:", data)
    return data
  else:
    print("Failed to getch jobs:", response.status_code, response.text)
    return {"SearchResult": {"SearchResultItems": []}}

def save_jobs(jobs):
  with open('jobs.json', 'w') as f:
    json.dump(jobs, f)

if __name__ == "__main__":
  job_data = fetch_jobs()
  jobs = job_data.get('SearchResult', {}).get('SearchResultItems', [])
  save_jobs(jobs)
  print(f"Saved {len(jobs)} jobs to jobs.json")