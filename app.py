import os

from flask import Flask, request, g, render_template, flash, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from forms import ReviewForm

import models

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'any string works here'

DEBUG = True
PORT = 8000


# Handle requests when the come in (before) and when they complete (after)
@app.before_request
def before_request():
  """Connect to the DB before each request."""
  g.db = models.DATABASE
  g.db.connect()

@app.after_request
def after_request(response):
  """Close the database connection after each request."""
  g.db.close()
  return response

@app.route('/')
def hello_world():
    form = ReviewForm()
    return render_template("review_form.html", title="New Review", form=form)

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)