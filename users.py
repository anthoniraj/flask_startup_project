from flask import Blueprint, render_template, request, session
from flask_login import LoginManager, login_user, logout_user, login_required
from models import User

usr = Blueprint('usr', __name__, template_folder='templates')

@usr.route("/form")
@login_required
def uform():    
    return render_template('form.html', name = session['name'])


@usr.route("/table")
@login_required
def utable():    
    return render_template('table.html', name = session['name'])
