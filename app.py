from flask import Flask, jsonify, request

import pipeline_predict as pp
import json
import pandas as pd
import config as cfg

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>hello_world!</p>"

# ruta para predecir
@app.route("/predecir", methods = ['POST'])
def predict_from_pp():
       json_data = request.get_json()
       dataframe = pd.json_normalize(json_data)
       data = dataframe

       data = data[cfg.FEATURES]
       print(dataframe)
       resultado = pp.predict(data)
       print(resultado)
       return jsonify({"Predicción": resultado})