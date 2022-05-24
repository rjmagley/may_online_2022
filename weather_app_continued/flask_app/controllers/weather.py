from flask_app import app

from flask import render_template
import requests

import os

@app.route('/')
def index():
    return render_template("weather_report.html")

@app.route('/weather/<string:city>')
def get_city_weather(city):
    weather_result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.environ.get('openweatherapikey')}")
    return render_template("result_partial.html", weather_data = weather_result.json())