import json
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


    # 'GET' routes
    def show_trending(self):
        pass
        #Need to decide how to rank/make a couple 
        #Order based on averageStar.currentRating, retrieve n max


    def search_by(self):
        data = request.get_json()
        search_term = list(data.keys())[0]
        
        if search_term == 'playlistName':
            _playlists = db.playlists.find(
                {'playlistName': data['playlistName']}
            )

        if search_term == 'playlistOwner':
            _playlists = db.playlists.find(
                {'playlistOwner': data['playlistOwner']}
            )

        if search_term == 'tags':
            _playlists = db.playlists.find(
                {'tags': data['tags']}
            )

        print(search_term, flush=True)
        if _playlists:
            playlists = [playlist for playlist in _playlists]
            return jsonify(playlists)

        return jsonify({'error': 'Playlist not found'})
        


    #Patch endpoints
    def patch(self):
        data = request.get_json()
        playlistName = data['playlistName']
        userRequesting = data['userRequesting']
        _patch_term = list(data.keys())
        _patch_term.remove('playlistName')
        _patch_term.remove('userRequesting')
        patch_term = _patch_term[0]
        
        #Check if playlist to interact exists
        to_patch = db.playlists.find_one({'playlistName': playlistName})
        if to_patch:
            
            # Check if who sent has editing access
            if to_patch['playlistOwner'] == userRequesting or userRequesting in to_patch['editingAccess']:


                # Patch accessibility
                if patch_term == 'public':
                    if data[patch_term] == 'True' or data[patch_term] == 'False':
                        playlist = db.playlists.find_one_and_update(
                            {'playlistName': playlistName},
                            {'$set': {patch_term: data[patch_term]}},
                            return_document = ReturnDocument.AFTER
                            )
                    else:
                        return jsonify({'error': 'You have to set public as either True or False (string)'})

                # Patch playlist name
                if patch_term == 'newName':
                    if db.playlists.find_one({'playlistName': data[patch_term]}):
                        return jsonify({'error': 'Playlist name already in use'}), 406
                    
                    playlist = db.playlists.find_one_and_update(
                            {'playlistName': playlistName},
                            {'$set': {'playlistName': data[patch_term]}},
                            return_document = ReturnDocument.AFTER
                            )
                    #find if the name is already used
                    
                
                # Patch theme
                if patch_term == 'playlistTheme':
                    playlist = db.playlists.find_one_and_update(
                            {'playlistName': playlistName},
                            {'$set': {patch_term: data[patch_term]}},
                            return_document = ReturnDocument.AFTER
                            )


                # Patch tags 
                if patch_term == 'tags':
                    
                    pass


                if patch_term == 'editingAccess':
                    pass


                if patch_term == 'chapters':
                    pass
            
            else:
                return jsonify({'error': 'You do not have editing access for this playlist'})

        else:
            return jsonify({'error': 'No playlist with that name'})


        print(playlist, flush=True)

        return jsonify(playlist)
        
    