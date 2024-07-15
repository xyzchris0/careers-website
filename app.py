from flask import Flask, render_template, jsonify

app = Flask(__name__)

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

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                          company_name='Cybersecurity Careers')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/roadmap")
def roadmap():
  return render_template('roadmap.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
