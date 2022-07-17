from crypt import methods
import pprint
import re
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pymongo import MongoClient
import os
from functools import wraps
import jwt

from temp.sample_data import users_model, playlist_model

app = Flask(__name__)
# app.secret_key = 'secretkeyforsession'
app.config['SECRET_KEY'] = 'secretkeyfortokens'


#Decorator for validate token
def token_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        data = request.get_json()
        token = data['token']

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            authorised = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])    
        except Exception as e:
            print(e, flush=True)
            return jsonify({'message': 'Token is invalid'}), 498

        return f(*args, **kwargs)
    return wrap




try:
    from dotenv import load_dotenv
    load_dotenv()
    client = MongoClient(
        host='mongodb_production',
        port=27017,
        username='root',
        password='pass',
        authSource='admin'
    )
    print(client)
    db=client.get_database('wewa')
    
except:
    print("We're in production now!")
    #THIS CONNECTS TO ATLAS
    connection_url = f"mongodb+srv://gio:{os.environ.get('password')}@cluster0.er7j3.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(connection_url)
    db = client.get_database('wewa')


# the two collections are playlist and users


CORS(app)
from models.user import routes

#Useless
# # Decorator for login session
# def login_required(f):
#     @wraps(f)
#     def wrap(*arg, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             return 'You need to be logged in!'
#     return wrap

# ## Routes





@app.route('/')
def home():
    return 'this works'

@app.route('/userSample', methods=['GET'])
def user_sample():
    return users_model, 200


@app.route('/playlistSample')
def playlist_sample():
    return playlist_model, 200




@app.route('/allusers')
# @login_required
def find_all():
        
    _users = db.users.find()


    users = [{'username': user['username']} for user in _users]

    return jsonify({'users': users}), 200



@app.route('/protected', methods=['POST'])
@token_required
def protected():
    return 'you have access to this'


@app.route('/unprotected')
def unprotected():
    return 'Access'





if __name__ == '__main__':
    app.run(port=4000, host='0.0.0.0')
