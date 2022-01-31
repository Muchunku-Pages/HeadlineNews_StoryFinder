from flask import render_template
from app import app

@app.route('/')
def index():
  '''
  The view root page function that renders the index page and its data contents
  '''
  message ='Howdy World'
  return render_template('index.html', message = message)