from app import app
from flask import render_template
from app.models.event_list import events
from app.models.event import Event


@app.route('/')
def index():
    return "Hello World"

@app.route('/events')
def events_list_all():
    return render_template("index.html", events=events)
