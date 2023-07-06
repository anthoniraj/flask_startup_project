from flask import Flask, session, render_template
from flask_wtf import CSRFProtect
from datetime import timedelta
from auth import entry, bcrypt, login_manager
from users import usr
from models import db, User

def create_app(object_name):
    app = Flask(__name__)      

    app.config['SECRET_KEY']='s@cr@tchu6ch'
    app.config['TEMPLATES_AUTO_RELOAD']=True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///church.db"
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True    
    
    csrf = CSRFProtect(app)
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(entry)    
    app.register_blueprint(usr) 
      
    @app.before_request
    def make_session_permanent():        
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=15)
    
    return app

if __name__ == '__main__':
    app = create_app('dev')
    # Debug True for Development, False for Production
    app.run(debug=True, host='0.0.0.0') 