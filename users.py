from flask import Blueprint, render_template, request, session
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_bcrypt import generate_password_hash
from models import User, db
from utils import log_user_activity

usr = Blueprint('usr', __name__, template_folder='templates')

@usr.route("/get_all_users")
@login_required
def get_all_users():  
    users = User.query.all()
    return render_template('users.html', name = session['name'], users = users)

@usr.route("/user_add", methods=['GET', 'POST'])
@login_required
def user_add():  
    if request.method == 'GET':        
        return render_template('user_add.html', name = session['name'])
    else:
        user = User()
        user.name = request.form['name']
        user.email = request.form['email']
        user.mobile = request.form['mobile']
        user.username= request.form['username']
        password = request.form['password']   
        user.password = generate_password_hash(password=password)     
        db.session.add(user)
        db.session.commit()
        log_user_activity(session['user_id'], user.name+" user added", request.remote_addr)
        users = User.query.all()
        return render_template('users.html', name = session['name'], users = users)

@usr.route("/user_update", methods=['GET', 'POST'])
@login_required
def user_update():  
    if request.method == 'GET':
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user_update.html', name = session['name'], user = user)
    else:
        user = User.query.get(request.form['id'])    
        user.name = request.form['name']
        user.email = request.form['email']
        user.mobile = request.form['mobile']     
        db.session.commit()
        log_user_activity(session['user_id'], user.name+" user details updated", request.remote_addr)
        users = User.query.all()
        return render_template('users.html', name = session['name'], users = users)

@usr.route("/user_delete")
@login_required
def user_delete():  
    id = request.args.get('id')
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    log_user_activity(session['user_id'], user.name+" user deleted", request.remote_addr)
    users = User.query.all()
    return render_template('users.html', name = session['name'], users = users)
