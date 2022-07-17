from flask import Flask
from app import app, token_required
from models.user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()
    



# @app.route('/user/signout')
# def signout():
#     return User().signout() 



@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/user/favourites', methods=['PATCH'])
@token_required
def update_favourites():
    return User().update_favourites()
