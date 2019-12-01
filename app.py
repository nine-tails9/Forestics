from flask import Flask, request, render_template
import requests
from flask_cors import CORS
import json
from flask_pymongo import PyMongo
from pymongo import MongoClient
from forest import findAcc
from apscheduler.scheduler import Scheduler
# Initialized Flask
app = Flask(__name__)


# CORS
CORS(app)


# Initialized Mongo
app.config['MONGO_DBNAME'] = 'forestics'
app.config["MONGO_URI"] = "mongodb://root:grofers16@ds033831.mlab.com:33831/forestics?retryWrites=false"
mongo = PyMongo(app)


# to be watched coords
coords = []

# Initialized scheduler
cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
# cron.start()
# @cron.interval_schedule(seconds=20)
# def job_function():
#     for lat, lng in coords:
#         updateData(lat, lng)


def updateData(lat, lng, location):
    name = lat + lng
    URL = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/' + lng + ',' + lat + ',15/800x600?access_token=pk.eyJ1IjoibmluZS10YWlsczkiLCJhIjoiY2szYnVkN200MHB0MDNwczEzdnpzdXUwZSJ9.y_Kl7N0k9MjGx6HI1YNITw'
    r = requests.get(url = URL, stream =True)
    if r.status_code == 200:
        with open("/code/dev/forestics/static/Images/" + name + '.png', 'wb') as f:
            f.write(r.content)
    findAcc('/code/dev/forestics/static/Images/' + name + '.png', name)
    mongo.db.images.insert({'path': name, 'name': location})

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/getpaths', methods=['GET'])
def getpaths():
    paths = mongo.db.images.find({})
    results = []
    for res in paths:
        results.append([res['path'], res['name']])
    return json.dumps(results)
    
 
@app.route('/addnew', methods=['GET'])
def addnew():
    coord = (request.args.get('lat'), request.args.get('lng'))
    coords.append(coord)
    updateData(coord[0], coord[1], request.args.get('name'))
    return '200'