from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required #makes sure an account is signed in to redirect to the profile page
def profile():
    return render_template('profile.html', name = current_user.name) 