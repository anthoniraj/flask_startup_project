from flask import Blueprint, render_template, request, session
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from models import User, UserActivity
from utils import log_user_activity
'''
    Author: Anthoniraj Amalanathan
    Date: Last Modified: 05-Jul-2023
    Description: Login Related Scripts
'''

entry = Blueprint('auth', __name__, template_folder='templates')
bcrypt = Bcrypt()
login_manager = LoginManager()

@entry.route('/', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html', msg="Please login to continue")
    else:
        username = request.form['username']
        password = request.form['password']

        #print(User.query.all())
        user = User.query.filter_by(username=username).first()
        if user:   
            #print(user)              
            if bcrypt.check_password_hash(user.password, password):  
                session['name'] = user.name
                session['user_id'] = user.id                
                login_user(user)
                log_user_activity(session['user_id'], "login success", request.remote_addr)
                return render_template('dashboard.html', name = session['name'])
            else:
                return render_template('login.html', msg="Invalid Credentials!")
        else:            
            return render_template('login.html', msg="Invalid Credentials!")


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.
    :param unicode user_id: user_id (username) user to retrieve
    """
    user = User()
    user.name = user_id
    return user

@entry.route("/dashboard")
@login_required
def dashboard():    
    #log_user_activity(session['user_id'], "dashboard accessed", request.remote_addr)
    return render_template('dashboard.html', name = session['name'])

@entry.route("/activity_logs")
@login_required
def activity_logs():
    id = session['user_id']
    logs = UserActivity.query.filter_by(user_id=id).order_by(UserActivity.timestamp.desc())
    return render_template('activity_logs.html', name = session['name'], logs = logs)

@entry.route("/logout")
@login_required
def logout():
    log_user_activity(session['user_id'], "logout success", request.remote_addr)
    logout_user()
    return render_template('login.html', msg="Please login to continue.")