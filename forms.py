from flask_wtf import FlaskForm as Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField
from models import Review

class ReviewForm(Form):
  plant = TextField("Species Name") 
  user = TextField("Posted By:")
  rating = IntegerField("Rating in start")
  text = TextAreaField("Insert Review Text body here")
  submit = SubmitField("create new Review")