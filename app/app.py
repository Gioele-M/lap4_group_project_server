import pprint
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pymongo import MongoClient
import os
from functools import wraps

from temp.sample_data import users_model, playlist_model

app = Flask(__name__)
app.secret_key = 'fbheifbeibfiefbiefbh'

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


# Decorator for login
def login_required(f):
    @wraps(f)
    def wrap(*arg, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return 'You need to be logged in!'
    return wrap

## Routes
from models.user import routes




@app.route('/')
def home():
    return 'this works'

@app.route('/userSample', methods=['GET'])
def user_sample():
    return users_model, 200


@app.route('/playlistSample')
def playlist_sample():
    return playlist_model, 200



# @app.route('/newuser')
# def new_user():
#     db.users.insert_one({'username': 'testusxxxer'})
#     return 'True', 204

@app.route('/allusers')
# @login_required
def find_all():
        
    _users = db.users.find()


    users = [{'username': user['username']} for user in _users]

    return jsonify({'users': users}), 200






if __name__ == '__main__':
    app.run(port=4000, host='0.0.0.0')
