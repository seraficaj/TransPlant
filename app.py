from flask import Flask, g
from flask import render_template, flash, redirect, url_for

from forms import  PostForm
import models


DEBUG = True
PORT = 8000

app = Flask(__name__)
app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

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



@app.route('/', methods=['GET', 'POST'])
def index():
  form = SubForm()
  if form.validate_on_submit():
    models.Plant.create(name=form.name.data.strip(), description=form.description.data.strip())

    flash("New sub registered. Called: {}".format(form.name.data))
    return redirect('/plants')
  return render_template('new_plant.html', title="New plant", form=form)

# 
@app.route('/plants')
@app.route('/plants/<plant>', methods=['GET', 'POST'])
def r(plant=None):
  if plant == None:
    plants = models.Plant.select().limit(100)
    return render_template("subs.html", plants=plants)
  else:
    # Find the right Sub
    plant_id = int(plant)
    plant = models.Plant.get(models.Plant.id == plant_id)
    plants = plant.posts





if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)