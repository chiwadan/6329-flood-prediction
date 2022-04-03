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
        myyear = request.form['YEAR']
        myannual = request.form['ANNUAL']
        model = load('app/flood-prediction.joblib')
        np_arr = np.array([myyear, myannual])
        predictions = model.predict([np_arr])  
        predictions_to_str = str(predictions)
        #return predictions_to_str
        return render_template('index.html', href2='The result of the flood prediction (year:'+str(myyear)+' , annual precipitation:'+str(myannual)+') is(1 means it will happen, 0 means it will not happen):'+predictions_to_str)

