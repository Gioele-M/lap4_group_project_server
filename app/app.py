import pprint
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)

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

users_model = {
    'username': 'Matteo',
    'hashedPassword': 'notsohashed',
    'userEmail': 'matteo@gmail.com', #primary key
    'token': 'token_string',
    'previousTokens': ['token1', 'token2'],
    'lastSelection': [{'selectedNote': 'chapter1', 'selectedPlaylist': 'playlistName'}],
    'recentPlaylist': [
        'playlist1'
        ],
    'favourites': ['playlistNameX', 'playlistNameY'],
    'achievement': ['badgeX', 'badgeY']
}


playlist_model = {
    'playlistName': 'playlistX',
    'playlistOwner': 'matteo@gmail.com',
    'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
    'public': True,
    'playlistTheme': '(0,0,0)',
    'tags': ['tag1', 'tag2'],
    'averageStars': {
        'currentRating': 3.5,
        'totalStars': 7,
        'totalRatings': 2
    },
    'userStars': [
        {'userEmail': 'gioele@gmail.com', 'rating': 4},
        {'userEmail': 'igor@gmail.com', 'rating': 3}
    ],
    'commentSection': [
        {
            'commentID': 1, #sequential
            'timestamp': '00.00.00.10.05.22',
            'username': 'Matteo',
            'userEmail': 'matteo@gmail.com',
            'comment': 'This playlist is great :)',
            'thread': [
                {
                    'timestamp': '00.00.00.10.05.22',
                    'username': 'Gio',
                    'userEmail': 'gioele@gmail.com',
                    'reply': 'great indeed!'
                },
                {   
                    'timestamp': '00.00.00.10.05.22',
                    'username': 'Igor',
                    'userEmail': 'igor@gmail.com',
                    'reply': 'Looks great but I would add another section!'
                }
            ]

        }
    ],
    'chapters': [
        {
            'chapter1': {
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter',
                'keywords': []
            }

            
        }
    ]
}

# result = db.users.insert_many(([
#     {
#         "username": 'Matteo',
#         "userEmail": "matteo@gmail.com",
#         "password": "pass"
#     },
#     {
#         "username": 'Gio',
#         "name": "gio@gmail.com",
#         "password": "pass"
#     },
#     {
#         "username": 'Igor',
#         "name": "igor@gmail.com",
#         "password": "pass"
#     },
# ]))



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
def find_all():
        
    _users = db.users.find()


    users = [{'username': user['username']} for user in _users]

    return jsonify({'users': users}), 200






if __name__ == '__main__':
    app.run(port=4000, host='0.0.0.0')
