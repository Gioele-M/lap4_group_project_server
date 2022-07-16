from crypt import methods
from flask import Flask, request
from app import app
from models.user.models import User

@app.route('/user/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return User().signup()
    return 'getuser'
 