import os
from flask import Flask, request, g, render_template, flash, redirect,url_for

from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash

from flask_cors import CORS

import models
from models import Review, userPlants

from forms import ReviewForm, SignUpForm, LoginForm, PlantForm, EditReviewForm



app = Flask(__name__, static_url_path='/static')
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
    g.user = current_user 

@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def landingPage():
    return render_template('landing.html')

@app.route('/swipe', methods=['GET', 'POST'])
def swipePage(swipe=None):
    form = PlantForm()

    if form.validate_on_submit():
        models.userPlants.create(user=g.user._get_current_object(),
                                content=form.content.data.strip())
    return render_template('swipe.html',swipe=swipe, form=form)


@app.route('/stream', methods=['GET','POST'])
def stream(username=None):

    form = ReviewForm()
    form2 = EditReviewForm()
        
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(form2.plant.data)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # reviews = models.Review.select()

    # idNumber2= request.args.get('idNumber2')

    # Review.plant = form2.plant.data
    
    reviews = models.Review.select()
    idNumber= request.args.get('idNumber')
    newValue= request.args.get('newValue')

    plant = Review.get(Review.id == 1)
    plant.plant = form2.plant.data
    plant.save()


    if form.validate_on_submit():
        models.Review.create(user=g.user._get_current_object(),
                                plant=form.plant.data,
                                rating= form.rating.data,
                                text=form.text.data)
    
    template = 'stream.html'
    if username and username != current_user.username:
        user = models.User.select().where(models.User.username == username).get()
        stream = user.reviews.limit(100)
    else:
        stream = current_user.get_stream().limit(100)
        user = current_user
    if username:
        template = 'profile.html'
    return render_template(template, stream=stream, form=form, form2= form2, username=username)

@app.route('/delete', methods=['GET'])
def delete():
    reviews = models.Review.select()
    idNumber= request.args.get('idNumber')
    if idNumber == Review.id:
        plant = Review.get(Review.id == idNumber)
        plant.delete_instance()

    return redirect(url_for('stream'))

# @app.route('/edit', methods=['GET'])
# def edit():
#     form2= EditReviewForm()
    
    reviews = models.Review.select()
    idNumber= request.args.get('idNumber')
    newValue= request.args.get('newValue')
    if idNumber == Review.id:
        plant = Review.get(Review.id == idNume)
        plant.plant = 'HELP'
        plant.save()

#     return redirect(url_for('stream'))


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

