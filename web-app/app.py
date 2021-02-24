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
                 + "eyJraWQiOiIyMDIxMDIxOTE4MzUiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC01NTAwMEFSRU1UIiwiaWQiOiJJQk1pZC01NTAwMEFSRU1UIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiOTk2ZDBhY2ItNjI3My00NjcxLWE0ZGYtYWE1NTM3YjBjNTIyIiwiaWRlbnRpZmllciI6IjU1MDAwQVJFTVQiLCJnaXZlbl9uYW1lIjoiTW9oYW1lZCIsImZhbWlseV9uYW1lIjoiRmF0aGFsbGFoIiwibmFtZSI6Ik1vaGFtZWQgRmF0aGFsbGFoIiwiZW1haWwiOiJtb2hhbWVkLmZhdGhhbGxhaEBlc3ByaXQudG4iLCJzdWIiOiJtb2hhbWVkLmZhdGhhbGxhaEBlc3ByaXQudG4iLCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiI5NzAxYzQxODMyMTc0MDAyYTI5NGMzYzMxZTM3ZDA1MyIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTYxNDE5ODIyOSwiZXhwIjoxNjE0MjAxODI5LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL29pZGMvdG9rZW4iLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.N4VLv9jzLUip3mfEDFX0LBl1yp3LEBqgI_1Xv7i1D09iAbQifTtLGFGrFFxo1ZFqridSZwFj509hJAI-XQw2Wsf70n7g7cT2Z2pvWMbK_5HAQexW_P_onSNLlToLBW_s9OwDVJ9yVAp1oCfMqD-W-qIoV5HaWKTvjOW7T2W9dd_tIWzjEFovmboW9FIOulxCrQbyolGF8bFjOhOOsu1A-orDH1qi3pEbfOzbq12xCSNPLdAo-KXrvM_4uEaoIi5jYANg4EUwYBgXe8TXOcYBq73yxYWqbawWhQQfSkGiPh8gsyXYgm8tVNSCiNu-Ey-_eFkH4Z-Grjxtk_1fKBsjDA"}


        python_object = [form.heartbeat.data, form.palpitation.data, form.chol.data,
        form.bmi.data, form.age.data, form.sex.data, form.family.data, form.smoker.data, form.exercise.data]



        userInput = []
        userInput.append(python_object)

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ["AVGHEARTBEATSPERMIN",
        "PALPITATIONSPERDAY","CHOLESTEROL","BMI","AGE","SEX","FAMILYHISTORY","SMOKERLAST5YRS","EXERCISEMINPERWEEK"],"values": userInput}]}

        
        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/524a0b40-ffdd-49b5-97d0-6dc56fd8f339/predictions?version=2021-02-24", json=payload_scoring, headers=header)
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
