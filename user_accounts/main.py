from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
from .models import User, Events

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required #makes sure an account is signed in to redirect to the profile page
def profile():
    usr = int(current_user.id)
    print(usr)
    event = Events.query.filter_by(user_id=usr) 
    return render_template('profile.html', data=event) 