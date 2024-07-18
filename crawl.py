import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file (only needed for local development)
load_dotenv()

# API Configuration
API_URL = "https://data.usajobs.gov/api/search"
HOST = "data.usajobs.gov"
USER_AGENT = os.getenv("USER_AGENT")
AUTH_KEY = os.getenv("AUTH_KEY")

def fetch_jobs():
    headers = {
        "Host": HOST,
        "User-Agent": USER_AGENT,
        "Authorization-Key": AUTH_KEY
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
        print("Failed to fetch jobs:", response.status_code, response.text)
        return {"SearchResult": {"SearchResultItems": []}}

def save_jobs(jobs):
    with open('jobs.json', 'w') as f:
        json.dump(jobs, f)
    print(f"Saved {len(jobs)} jobs to jobs.json")

if __name__ == "__main__":
    job_data = fetch_jobs()
    jobs = job_data.get('SearchResult', {}).get('SearchResultItems', [])
    save_jobs(jobs)
