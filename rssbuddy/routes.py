from rssbuddy import app
from flask import render_template

@app.route('/')
def home_page():
    render_template('home.html')