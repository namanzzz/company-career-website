from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Software Engineer 1',
    'location':'Bengaluru, India',
    'salary':'RS 1000000',
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Bengaluru, India',
    # 'salary': 'RS 1500000',
  },
  {
    'id':3,
    'title': 'Senior Software Engineer',
    'location':'Delhi, India',
    'salary': 'RS 2000000',
  },
  {
    'id':4,
    'title': 'Software Engineer Intern',
    'location':'Bengaluru, India',
    'salary': 'RS 500000',
  },
  {
    'id':5,
    'title': 'Software Engineer 3',
    'location':'New york, United States',
    'salary': '$340,000',
  },
  {
    'id':6,
    'title': 'Backend Engineer',
    'location':'Remote',
    'salary': '$120,000',
  },
  
]



@app.route("/")

def hello_cdesk():
  return render_template('home.html', jobs = JOBS, company_name='Cdesk')

@app.route("/api/jobs")

def list_jobs():
  return jsonify(JOBS)
  



if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)  