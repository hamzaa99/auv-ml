import logging

import numpy as np
import pandas as pd
from flask import Flask, request, render_template,jsonify
from sklearn import preprocessing
import pickle
import json

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
villes = pd.read_csv('data/merged/test.csv', delimiter=",", header=0, index_col='CODGEO', dtype={'CODGEO': 'str'})




@app.route('/')
def home():
    return "welcome home"


@app.route('/predict', methods=['POST'])
def predict():

    payload = request.get_json()
    labels = model.predict(villes)
    ville = villes.loc[payload['ville']]
    labelPrediction = model.predict([ville])

    cluster_map = pd.DataFrame()
    cluster_map['data_index'] = villes.index
    cluster_map['cluster'] = model.labels_

    result = cluster_map[cluster_map.cluster == labelPrediction[0]]


    return result[:10].to_json(orient="split")



if __name__ == "__main__":
    app.run(debug=True)