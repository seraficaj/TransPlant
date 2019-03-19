import os

from flask import Flask, request, g, render_template, flash, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from forms import ReviewForm

app = Flask(__name__)
CORS(app)

DEBUG = True
PORT = 8000

app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

@app.route('/')
def swipePage(swipe=None):
    form = ReviewForm()
    return render_template('swipe.html',swipe=swipe, form=form)



if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)