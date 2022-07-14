from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print("We're in production now!")

connection_url = f"mongodb+srv://gio:{os.environ.get('password')}@cluster0.er7j3.mongodb.net/?retryWrites=true&w=majority"

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
    db.users.insert_one({'username': 'testusxxxer'})
    return 'True', 204


