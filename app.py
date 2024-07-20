from flask import Flask, render_template, jsonify
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def load_jobs():
    if os.path.exists('jobs.json'):
        with open('jobs.json', 'r') as f:
            jobs = json.load(f)
        print("Jobs loaded:", jobs)  # Debug print statement
        return jobs
    else:
        print("jobs.json file not found")
        return []

@app.route("/")
def home():
    jobs = load_jobs()
    return render_template('home.html', company_name="Go Remote Cyber", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(load_jobs())

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
