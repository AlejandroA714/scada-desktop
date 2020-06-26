from flask_pymongo import PyMongo
from flask import Flask, jsonify,request, make_response


app = Flask(__name__) # APP

@app.route('/')
def index():
    try:
        answer = []
        for s in mongo.db.controles_scada.find({}):
            answer.append({'Id' : str(s['_id']),'Nombre':s['Nombre'],'Drivers': s['Drivers'],'DriversCount': len(s['Drivers'])  })
    except Exception as e:
        pass
    return jsonify(answer)

app.config['MONGO_URI'] =  "mongodb://alejandro:<password>@ds039707.mlab.com:39707/heroku_pmb9h46c"
mongo = PyMongo(app) ## Inicia una estancia de Mongo


app.run()
