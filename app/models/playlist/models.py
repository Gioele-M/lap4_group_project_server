from flask import Flask, jsonify, request
from app import db
from pymongo import ReturnDocument
from app import app, db
import uuid


class Playlist:
    
    #Temp route
    def showall(self):
        _playlists = db.playlists.find()
        playlists = [{'playlistName': playlist['playlistName']} for playlist in _playlists]
        return jsonify(playlists)



    # POST route
    def create_playlist(self):
        data = request.get_json()

        new_playlist = {
            "_id": uuid.uuid4().hex,
            'playlistName': data['playlistName'],
            'playlistOwner': data['email'],
            'editingAccess': [],
            'public': 'True',
            'playlistTheme': '(0,0,0)',
            'tags': [],
            'averageStars': {
                'currentRating': 0,
                'totalStars': 0,
                'totalRatings': 0
            },
            'userStars': [],
            'commentSection': [],
            'chapters': []
        }

        #Chack if playlist name already exists
        if db.playlists.find_one({'playlistName': new_playlist['playlistName']}):
            return jsonify({'error': 'Playlist name already taken'}), 406

        #add playlist to db
        if db.playlists.insert_one(new_playlist):
            return jsonify(new_playlist),200

        # if anything went wrong
        return jsonify({'error': 'Add playlist failed'}), 400


    # GET routes
    def show_trending(self):
        pass
        #Need to decide how to rank/make a couple 
        #Order based on averageStar.currentRating, retrieve n max


    def search_by_name(self):
        data = request.get_json()
        #Finds one bc playlists names are unique
        playlist = db.playlists.find_one(
            {'playlistName': data['playlistName']}
        )
        print(playlist, flush=True)
        if playlist:
            return jsonify(playlist)

        return jsonify({'error': 'Playlist not found'})
        