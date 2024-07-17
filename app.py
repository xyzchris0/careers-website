from flask import Flask, render_template, jsonify
import requests
import os
from dotenv import load_dotenv 

app = Flask(__name__)

API_URL = "https://data.usajobs.gov/api/search"
HOST = "data.usajobs.gov"
USER_AGENT = os.environ.get("USER_AGENT") #Load from variables 
AUTH_KEY = os.environ.get("AUTH_KEY") #Load from variables 

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Washington, D.C.',
        'salary': '$100,000',
    },
    {
        'id': 2,
        'title': 'CyberSecurity Analyst',
        'location': 'Washington, D.C.',
        'salary': '$140,000',
    },
    {
        'id': 3,
        'title': 'Security Engineer',
        'location': 'Washington, D.C.',
        'salary': '$110,000',
    }
]

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
        print("API response:", data)  # Debug print statement
        return data
    else:
        print("Failed to fetch jobs:", response.status_code, response.text)
        return {"SearchResult": {"SearchResultItems": []}}

@app.route("/")
def home():
    job_data = fetch_jobs()
    jobs = job_data.get('SearchResult', {}).get('SearchResultItems', [])
    print("Jobs data:", jobs)  # Debug print statement
    return render_template('home.html', company_name="Go Remote Cyber", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(fetch_jobs())

@app.route("/roadmap")
def roadmap():
    return render_template('roadmap.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/bestcertifications")
def bestcertifications():
    return render_template('bestcertifications.html')

@app.route("/joblandscape")
def joblandscape():
    return render_template('joblandscape.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)  # Use a different port if 5000 is in use
