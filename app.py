import os
from flask import Flask, request, g, render_template, flash, redirect,url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash

from flask_cors import CORS

from forms import ReviewForm, SignUpForm, LoginForm
import models

app = Flask(__name__)
CORS(app)

DEBUG = True
PORT = 8000

app.secret_key = 'adkjfalj.adflja.dfnasdf.asd'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.before_request
def before_request():
    g.db= models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def swipePage(swipe=None):
    form = ReviewForm()
    return render_template('swipe.html',swipe=swipe, form=form)

@app.route('/signup', methods=('GET', 'POST'))
def signupPage():
    form = SignUpForm()
    if form.validate_on_submit():
        flash('signup successful')
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
            )
        return redirect(url_for('swipePage'))

    return render_template('signup.html',form=form)

@app.route('/login', methods=('GET', 'POST'))
def loginPage():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Not a match")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Logged In!")
                return redirect(url_for('swipePage'))
            else:
                flash("Not a match!")

    return render_template('login.html',form=form)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged Out")
    return redirect(url_for('swipePage'))



if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(
            username='rroy',
            email="rhea@rhea.com",
            password='password',
            admin=True
            )
    except ValueError:
        pass
    
    app.run(debug=DEBUG, port=PORT)
