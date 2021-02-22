from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
auth = Blueprint('auth',__name__)

@auth.route('/login') #access login page
def login():
    return render_template('login.html')

#@auth.route('/login', methods = ['POST'])
#def login_post():
    
@auth.route('/signup') #access sign up page
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods = ['POST']) #create users on the database
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() #check if the email is already registered

    if user: #if email is registered, redirect to login page
        return redirect(url_for('auth.login')) 

@auth.route('/logout') #log out of account
def logout():
    return redirect(url_for('main.index'))