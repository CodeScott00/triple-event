from app import app
from flask import render_template

@app.route('/')
def index():
    return "Hello World"

@app.route('/events')
def events():
    return render_template "index.html"
