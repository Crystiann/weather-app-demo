import json

from flask import  Flask #importa obiectul Flask din modulul flask

import weather

# import sys

# print(">>", sys.path()) #nu este corect definit


app = Flask(__name__)

@app.route("/") # / inseamna ca ruleaza din root
def hello():
    return "Hello,World!"


@app.route("/weather/") # atentie la /weather/ sa fie intre back slah sau calea buna
def weather_route(): #numele la aceasta functie trebuie sa fie diferit de numele la functia importata
    temp = json.dumps(weather.weather())
    return temp

@app.route("/weather/my-cities/") #route defineste ruta
def weather_multiplecities():
    return "Cluj: 15, New Yourk: 10"