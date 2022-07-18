import json
from operator import is_
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
                    old_tags = to_patch['tags']
                    if data[patch_term] in old_tags:
                        return jsonify({'error': 'Tag already present'})
                    old_tags.append(data[patch_term])
                    playlist = db.playlists.find_one_and_update(
                            {'playlistName': playlistName},
                            {'$set': {patch_term: old_tags}},
                            return_document = ReturnDocument.AFTER
                            )
                    


                if patch_term == 'editingAccess':
                    has_access = to_patch['editingAccess']
                    if data[patch_term] in has_access:
                        return jsonify({'error': 'User has already access'})
                    has_access.append(data[patch_term])
                    playlist = db.playlists.find_one_and_update(
                            {'playlistName': playlistName},
                            {'$set': {patch_term: has_access}},
                            return_document = ReturnDocument.AFTER
                            )


                ####### NEED to discuss this
                # Do we want to patch the chapter changing stuff in it?
                # Check how to fix if deleting
                if patch_term == 'chapters':
                    old_chapters = to_patch[patch_term]

                    #Check if it has chapter with same id
                    #is_patch = any(x['chapterId'] == data[patch_term]['chapterId'] for x in old_chapters)
                    is_patch = next((x for x in old_chapters if x['chapterId'] == data[patch_term]['chapterId']), False)

                    #if it has to be patched replace it otherwise add it to the old chapters
                    if is_patch:
                        index = old_chapters.index(is_patch)
                        old_chapters[index] = data[patch_term]
                        playlist = db.playlists.find_one_and_update(
                            {'playlistName': playlistName},
                            {'$set': {patch_term: old_chapters}},
                            return_document = ReturnDocument.AFTER
                            )
                    else:
                        old_chapters.append(data[patch_term])

                        playlist = db.playlists.find_one_and_update(
                                {'playlistName': playlistName},
                                {'$set': {patch_term: old_chapters}},
                                return_document = ReturnDocument.AFTER
                                )
                    
            
            else:
                return jsonify({'error': 'You do not have editing access for this playlist'})

        else:
            return jsonify({'error': 'No playlist with that name'})


        print(playlist, flush=True)

        return jsonify(playlist)
        
    


    def patch_all(self):
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

            # Patch comments
            if patch_term == 'commentSection':
                old_comments = to_patch[patch_term]

                # check if there is a comment with the same id
                is_patch = next((x for x in old_comments if x['commentID'] == data[patch_term]['commentID']), False)

                #If has to be patched replace it otherwise add it to the old chapters
                if is_patch:
                    index = old_comments.index(is_patch)
                    old_comments[index] = data[patch_term]
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {patch_term: old_comments}},
                        return_document = ReturnDocument.AFTER
                    )
                else:
                    old_comments.append(data[patch_term])
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {patch_term: old_comments}},
                        return_document = ReturnDocument.AFTER
                    )

            #Patch starts
            if patch_term == 'userStars':
                old_ratings = to_patch[patch_term]

                #check if there is a rating with the same useremail
                is_patch = next((x for x in old_ratings if x['userEmail'] == userRequesting), False)

                #If it has to be patched change the rating otherwise append new rating 
                if is_patch:
                    index = old_ratings.index(is_patch)
                    old_ratings[index] = {'userEmail': userRequesting, 'rating': data[patch_term]}
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {patch_term: old_ratings}},
                        return_document = ReturnDocument.AFTER
                    )
                else:
                    old_ratings.append({'userEmail': userRequesting, 'rating': data[patch_term]})
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {patch_term: old_ratings}},
                        return_document = ReturnDocument.AFTER
                    )

        else:
            return jsonify({'error': 'No playlist with that name'})


        print(playlist, flush=True)

        return jsonify(playlist)
