from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, TextField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError

class PredictForm(FlaskForm):
	heartbeat = IntegerField("AVGHEARTBEATSPERMIN")
	palpitation = IntegerField("PALPITATIONSPERDAY")
	chol = IntegerField("CHOLESTEROL")
	bmi = IntegerField("BMI")
	age = IntegerField("AGE")
	sex = IntegerField("SEX")
	family = StringField("FAMILYHISTORY")
	smoker = StringField("SMOKERLAST5YRS")
	exercise = IntegerField("EXERCISEMINPERWEEK")
	submit = SubmitField('Predict')
	abc = ""
	chtrue=0
	chfalse=0





 ##  age = IntegerField('Age')
  # sex = StringField('Sex')
   #bmi = DecimalField('BMI')
   #children = IntegerField('Children')
   #smoker = StringField('Smoker')
   #region = StringField('Region')
  # submit = SubmitField('Predict')
  # abc = "" # this variable is used to send information back to the front page
