from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User, Events
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth',__name__)

@auth.route('/login') #access login page
def login():
    return render_template('login.html')

@auth.route('/login', methods = ['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first() #searches for the user in the db by querying the email

    if not user or not check_password_hash(user.password, password):
        flash('Login details are incorrect. Please try again.')
        return redirect(url_for('auth.login'))

    login_user(user)

    return redirect(url_for('main.profile'))

@auth.route('/create_event')
def create_events():
    return render_template('create_events.html')

@auth.route('/create_event', methods=['POST'])
def create_events_post():
    name = request.form.get('name')
    event_name = request.form.get('event_name')
    date_time = request.form.get('date_time')
    caption = request.form.get('caption')

    new_event = Events(name=name, event_name = event_name, date_time = date_time, caption=caption)
    db.session.add(new_event)
    db.session.commit()
    return redirect(url_for('main.index'))


@auth.route('/signup') #access sign up page
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods = ['POST']) #create users on the database
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() #check if the email is already registered

    if user: #if email is registered, inform user and redirect to login page
        flash('Email address in use!')
        return redirect(url_for('auth.signup'))
    else: #else create user using credentials entered in form
        #we create a user in the database with the credentials provided and password is hashed/encrypted for security reasons 
        new_usr = User(email=email, name=name, password = generate_password_hash(password, method='sha256'))
        db.session.add(new_usr)
        db.session.commit()
        return redirect(url_for('auth.login')) 

@auth.route('/logout') #log out of account
def logout():
    logout_user()
    return redirect(url_for('main.index'))