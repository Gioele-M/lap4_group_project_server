from crypt import methods
from flask import Flask, request
from app import app
from models.user.models import User

@app.route('/user/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return User().signup()
    return 'get user method '




@app.route('/user/signout')
def signout():
    return User().signout() 



@app.route('/user/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return User().login()
    return 'get login method '

#Request
# {
#   "email": "gio@gio.com",
#   "password": "pass"
# }
