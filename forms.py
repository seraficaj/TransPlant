from flask_wtf import FlaskForm as Form
from wtforms import TextField, TextAreaField, SubmitField


class ReviewForm(Form):
  review = TextAreaField("Review this plant: ")
  submit = SubmitField('Submit Review')
