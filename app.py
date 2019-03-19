import os

from flask import Flask, request, g, render_template, flash, redirect,url_for
from flask_cors import CORS
from forms import ReviewForm

import models
from models import Review

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

@app.route('/review', methods=['GET', 'POST'])
def make_review():
    form = ReviewForm()

    if form.validate_on_submit():
      # if it is, we create a new review
      print(
        form.plant.data,
        form.user.data,
        form.rating.data,
        form.text.data
      )
      models.Review.create(
        plant=form.plant.data.strip(),
        user=form.user.data.strip(),
        rating=form.rating.data,
        text=form.text.data.strip()
      )
      flash("NEW REVIEW {}".format(form.plant.data))
      # and redirect to the main reviews index
      return redirect('/reviews')
      
    # if the submission isn't valid, send the user back to the original view
    return render_template("review_form.html", title="New Review", form=form)

@app.route('/reviews')
def show_reviews():
  reviews = models.Review.select().limit(100)
  return render_template("reviews.html", reviews=reviews)

if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)