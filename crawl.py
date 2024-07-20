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
        "Keyword": "Remote",
        "LocationName": "Remote"
    }
    response = requests.get(API_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print("API response:", json.dumps(data, indent=2))  # Pretty print the API response for debugging
        jobs = data.get('SearchResult', {}).get('SearchResultItems', [])
        return {"SearchResult": {"SearchResultItems": jobs}}
    else:
        print("Failed to fetch jobs:", response.status_code, response.text)
        return {"SearchResult": {"SearchResultItems": []}}

def save_jobs(jobs):
    with open('jobs.json', 'w') as f:
        json.dump(jobs, f)

if __name__ == "__main__":
    job_data = fetch_jobs()
    jobs = job_data.get('SearchResult', {}).get('SearchResultItems', [])
    print(f"Total jobs fetched: {len(jobs)}")  # Print the number of jobs fetched
    for job in jobs:  # Print details of each job to check if they are remote
        print(f"Job Title: {job['MatchedObjectDescriptor']['PositionTitle']}")
        print(f"Organization: {job['MatchedObjectDescriptor']['OrganizationName']}")
        locations = job['MatchedObjectDescriptor'].get('PositionLocation', [])
        for location in locations:
            print(f"Location: {location['LocationName']}")
        print("-----")
    save_jobs(jobs)
    print(f"Saved {len(jobs)} jobs to jobs.json")
