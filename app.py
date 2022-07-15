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

users_model = {
    'username': 'Matteo',
    'hashedPassword': 'notsohashed',
    'userEmail': 'matteo@gmail.com',
    'token': 'token_string',
    'previousTokens': ['token1', 'token2'],
    'lastSelection': {'selectedNote': 'chapter1', 'selectedPlaylist': 'playlistName'},
    'recentNotes': [
        {'selectedNote': 'chapter2', 'selectedPlaylist': 'playlistNameX'}, 
        {'selectedNote': 'chapter3', 'selectedPlaylist': 'playlistNameY'}
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
            'username': 'Matteo',
            'userEmail': 'matteo@gmail.com',
            'comment': 'This playlist is great :)',
            'thread': [
                {
                    'username': 'Gio',
                    'userEmail': 'gioele@gmail.com',
                    'reply': 'great indeed!'
                },
                {
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
                'text': 'This is the section with the notes on the first chapter'
            }

            
        }
    ]
}





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


# def find_all():
#     users = db.users.find()
#     return str(users), 200
