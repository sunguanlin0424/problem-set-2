from flask import Flask, render_template, json, request
from flask import Markup
import requests

app = Flask(__name__)
app.config["DEBUG"] = False

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/food")
def food():
    return render_template('food.html')

@app.route("/route")
def route():
    return render_template('route.html')

@app.route("/note1")
def note1():
    return render_template('note1.html')

@app.route("/note2")
def note2():
    return render_template('note2.html')

@app.route("/note3")
def note3():
    return render_template('note3.html')

@app.route("/map1")
def map1():
    return render_template('map1.html')

@app.route("/map2")
def map2():
    return render_template('map2.html')

@app.route("/map3")
def map3():
    return render_template('map3.html')

@app.route("/table")
def table():

   r = requests.get('https://api.airtable.com/v0/appnz0jma5BilSbeD/%E6%99%AF%E7%82%B9?api_key=key0eGGPlI2X82Vz3')
   dict = r.json()
   dataset = []
   for i in dict['records']:
           dict = i['fields']
           dataset.append(dict)

   return render_template('table.html', entries=dataset)