from flask_wtf import FlaskForm as Form

from wtforms import TextField, IntegerField, TextAreaField, SubmitField
from models import Review

from models import User, userPlants

from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)


class ReviewForm(Form):
  plant = TextField("Species Name")
  rating = IntegerField("Rating (Integer between 1 and 5)")
  text = TextAreaField("Review Text")
  submit = SubmitField("Create New Review")

class EditReviewForm(Form):
  plant = TextField("Species Name")
  rating = IntegerField("Rating (Integer between 1 and 5)")
  text = TextAreaField("Review Text")
  idNumber = IntegerField("idNumber")
  submit2 = SubmitField("Save Edit")

class EditProfileForm(Form):
    username = TextField("Username")
    city = TextField("City")
    submit4 = SubmitField("Save Profile")


class PlantForm(Form):
    userPlants= TextField("Enter Plants Here")

def name_exists(form, field):
    if User.select().where(User.username == field.data).exists():
        raise ValidationError('User with that name already exists.')

def email_exists(form, field):
    if User.select().where(User.email == field.data).exists():
        raise ValidationError('User with that email already exists.')

class SignUpForm(Form):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Regexp(
                r'^[a-zA-Z0-9_]+$',
                message=("Username should be one word, letters, "
                         "numbers, and underscores only.")
            ),
            name_exists
        ])
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(),
            email_exists
        ])
    city = StringField(
        'City',
        validators=[
            DataRequired(),
        ])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=2),
            EqualTo('password2', message='Passwords must match')
        ])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()]
    )

class LoginForm(Form):
    email = StringField('Email', validators= [DataRequired(),Email()])
    password = PasswordField ('Password', validators= [DataRequired()])

