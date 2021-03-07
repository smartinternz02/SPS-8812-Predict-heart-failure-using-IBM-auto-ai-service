from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
import pygal 
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJraWQiOiIyMDIxMDIxOTE4MzUiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC01NTAwMEFSRU1UIiwiaWQiOiJJQk1pZC01NTAwMEFSRU1UIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiZjU3YjhhM2YtYWU4OS00OTIxLWE3MjQtOTMzY2M1Y2E1YzgzIiwiaWRlbnRpZmllciI6IjU1MDAwQVJFTVQiLCJnaXZlbl9uYW1lIjoiTW9oYW1lZCIsImZhbWlseV9uYW1lIjoiRmF0aGFsbGFoIiwibmFtZSI6Ik1vaGFtZWQgRmF0aGFsbGFoIiwiZW1haWwiOiJtb2hhbWVkLmZhdGhhbGxhaEBlc3ByaXQudG4iLCJzdWIiOiJtb2hhbWVkLmZhdGhhbGxhaEBlc3ByaXQudG4iLCJhdXRobiI6eyJzdWIiOiJtb2hhbWVkLmZhdGhhbGxhaEBlc3ByaXQudG4iLCJpYW1faWQiOiJpYW0tNTUwMDBBUkVNVCIsIm5hbWUiOiJNb2hhbWVkIEZhdGhhbGxhaCIsImdpdmVuX25hbWUiOiJNb2hhbWVkIiwiZmFtaWx5X25hbWUiOiJGYXRoYWxsYWgiLCJlbWFpbCI6Im1vaGFtZWQuZmF0aGFsbGFoQGVzcHJpdC50biJ9LCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiI5NzAxYzQxODMyMTc0MDAyYTI5NGMzYzMxZTM3ZDA1MyIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTYxNTEzNDk5MCwiZXhwIjoxNjE1MTM4NTkwLCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL29pZGMvdG9rZW4iLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.JK8Df5rCwuN5D2fr7kDJJw-lgsGmmTu9nFChm8xiXqQEkIUpRZEOPGM01xN90i1wazESKxbBkSqOZZ23cgRS_NCAfiKtg11YUAH23IB-2grDm-HhTxSfHMmj3pk0TNlQpiaH5e3TLxlQT2uFUW2naATe6cS1TX24aP1Hn9ln46wG8hPhC8_vDMy9nQeWbAscR31dm1MJiAksBpk5k-jgv649qHKR29VhCy4yB2SYREar7iR1Jp46NDQj6RlpNMVM3IpwHhrXx8wjpdk2zA6cjWZRWE0yJafKNKKG43xfitV7Mxw_EMEq90VGcVa3PSrf6OuXBgFCBhRGaSRYD2W1VA"}


        python_object = [form.heartbeat.data, form.palpitation.data, form.chol.data,
        form.bmi.data, form.age.data, form.sex.data, form.family.data, form.smoker.data, form.exercise.data]



        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["AVGHEARTBEATSPERMIN",
        "PALPITATIONSPERDAY","CHOLESTEROL","BMI","AGE","SEX","FAMILYHISTORY","SMOKERLAST5YRS","EXERCISEMINPERWEEK"],"values": userInput}]}

        
        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7df29f40-7a2e-4bd1-86cb-084a4997aab4/predictions?version=2021-03-07", json=payload_scoring, headers=header)
        output = json.loads(response_scoring.text)
        print("Scoring response")
        print(response_scoring.json())
        print(output)
        form.abc=output
        #ffres = StringField("prediction")
       # form.abc=output
      # print(output)

   
        for key in output:
          ab = output[key]
        

        for key in ab[0]:
          bc = ab[0][key]
        
        
        #form.abc=ffres
        form.chtrue= bc[0][1][0]
        form.chfalse=bc[0][1][1]
      
        form.abc = bc[0][0] # this returns the response back to the front page
        return render_template('index.html', form=form)
