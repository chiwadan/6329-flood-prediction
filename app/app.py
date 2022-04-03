from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from joblib import load
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href2='')
    else:
        year = request.form['YEAR']
        annual = request.form['ANNUAL']
        print('year')
        print('annual')
        model = load('app/flood-prediction.joblib')
        np_arr = np.array([year, annual])
        predictions = model.predict([np_arr])  
        predictions_to_str = str(predictions)
        #return predictions_to_str
        return render_template('index.html', href2='At the (year:'+str(year)+' ,annual precipitation:'+str(annual)+'), the result of predicting flood is (1 means it will happen, 0 means it will not happen):'+predictions_to_str)

