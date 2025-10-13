import pickle
from flask import Flask, request
import os

app = Flask(_name_)

def model_infrence(data):
    with open('model.pkl','rb') as models:
        pred_model = pickle.load(models)

    predictions = pred_model.predict(data)

    return pedictions

@app.route('/',methods = ['POST'])
def funcs():
    return 'Serrver is UP'

@app.route('/predictions',methods = ['POST'])
def preds():
    s1 = eval(request.form[''])
    sw = eval(request.form[''])
    p1 = eval(request.form[''])
    pw = eval(request.form[''])

    if model == 'Logistic Regression':
        model = 'model'
    elif model == 'Random Forest':
        model = 'rf_model'
    else:pass

    data = [[s1,sw,p1,pw]]

    predicted_values = model_inference(datas,model)

    return f'Predicted Value: {predicted_values},Used Model{model}'

port = int(os.environ.get("PORT", 8000))
app.run(host = '0.0.0.0', port = port)
