from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
#{os.environ.get('password')}

connection_url = f"mongodb+srv://gio:gio@cluster0.er7j3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_url)

db = client.get_database('wewa')
# the two collections are playlist and users


CORS(app)

@app.route('/', methods=['GET'])
def home_route():
    users = db.users.find()
    return str(users), 200



@app.route('/newuser')
def new_user():
    db.users.insert_one({'username': 'testuser'})
    return 'True', 204


