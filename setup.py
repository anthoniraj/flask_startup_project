from main import db, create_app
from models import User
from getpass import getpass
from flask_bcrypt import generate_password_hash

'''
    Author: Anthoniraj Amalanathan
    Date: Last Modified: 05-Jul-2023
    Description: Run this script first to create user table and admin account
'''

app = create_app('dev')

def get_user_details():
    user = User()
    user.name = input("Enter Fullname: ")
    user.username = input("Enter Fullname: ")
    password = getpass(prompt='Enter Password: ')
    user.password = generate_password_hash(password=password)
    user.email = input("Enter Email: ")
    user.mobile = input("Enter Mobile Number: ")
    return user 

def create_user():
    with app.app_context():
        db.create_all()
        # Create Admin User Account        
        user = get_user_details()
        db.session.add(user)
        db.session.commit()

if __name__ == '__main__':
    create_user()