import json
from operator import is_
from sys import flags
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
                    old_stars = old_ratings[index]['rating']
                    old_ratings[index] = {'userEmail': userRequesting, 'rating': data[patch_term]}

                    #set average stars
                    average_stars = to_patch['averageStars']
                    average_stars['totalStars'] += data[patch_term] - old_stars
                    average_stars['currentRating'] = average_stars['totalStars'] / average_stars['totalRatings']


                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {patch_term: old_ratings}},
                        return_document = ReturnDocument.AFTER
                    )

                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {'averageStars': average_stars}}, 
                        return_document = ReturnDocument.AFTER
                    )
                else:
                    old_ratings.append({'userEmail': userRequesting, 'rating': data[patch_term]})

                    #set average stars
                    average_stars = to_patch['averageStars']
                    average_stars['totalStars'] += data[patch_term]
                    average_stars['totalRatings'] += 1
                    average_stars['currentRating'] = average_stars['totalStars'] / average_stars['totalRatings']
                    
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {patch_term: old_ratings}},
                        return_document = ReturnDocument.AFTER
                    )
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {'averageStars': average_stars}}, 
                        return_document = ReturnDocument.AFTER
                    )

        else:
            return jsonify({'error': 'No playlist with that name'}), 406


        print(playlist, flush=True)

        return jsonify(playlist)



    def delete_auth(self):
        data = request.get_json()
        playlistName = data['playlistName']
        userRequesting = data['userRequesting']
        _delete_term = list(data.keys())

        _delete_term.remove('playlistName')
        _delete_term.remove('userRequesting')
        delete_term = _delete_term[0]

        to_delete = db.playlists.find_one({'playlistName': playlistName})

        
        if to_delete:
            #check user requesting has editing access
            # Check if who sent has editing access, else error
            if to_delete['playlistOwner'] == userRequesting or userRequesting in to_delete['editingAccess']:
                
                #Remove tags
                if delete_term == 'tags':
                    tags = to_delete[delete_term]
                    if data[delete_term] not in tags:
                        return jsonify({'error': 'This tag does not exist'}), 406
                    tags.remove(data[delete_term])
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {delete_term: tags}},
                        return_document = ReturnDocument.AFTER
                    )

                #Remove chapter
                if delete_term == 'chapters':
                    chapterN = data[delete_term]
                    chapters = to_delete[delete_term]
                    #Check if there is a chapter with the ID to be removed
                    # check if there is a comment with the same id
                    is_delete = next((x for x in chapters if x['chapterId'] == chapterN), False)
                    
                    if not is_delete:
                        return jsonify({'error': 'This chapter does not exist'}), 406

                    if not chapterN == len(chapters):
                        for chapter in chapters:
                            if chapter['chapterId'] > chapterN:
                                chapter['chapterId'] -= 1

                    
                    chapters.remove(is_delete)
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {delete_term: chapters}},
                        return_document = ReturnDocument.AFTER
                    )


                #Remove playlist
                if delete_term == 'playlist':
                    if to_delete['playlistOwner'] != userRequesting:
                        return jsonify({'error': 'Only owners can delete playlists!'}), 403
                    
                    playlist = db.playlists.delete_one({'playlistName': playlistName})
                    return jsonify({'message': 'Playlist deleted'}), 404




            else:
                return jsonify({'error': 'You do not have editing access for this playlist'}), 403

        else:
            return jsonify({'error': 'No playlist with that name'}), 404


        print(playlist, flush=True)

        return jsonify(playlist), 200




    def delete_for_all(self):
        data = request.get_json()
        playlistName = data['playlistName']
        userRequesting = data['userRequesting']
        _delete_term = list(data.keys())

        _delete_term.remove('playlistName')
        _delete_term.remove('userRequesting')
        delete_term = _delete_term[0]

        to_delete = db.playlists.find_one({'playlistName': playlistName})

        
        if to_delete:

            if delete_term == 'thread':
                #Check if user has comment in thread
                comments = to_delete['commentSection']

                comment_requested = next((x for x in comments if x['commentID'] == data[delete_term]), False)

                if comment_requested:
                    deleted = False
                    for thread in comment_requested['thread']:
                        if thread['userEmail'] == userRequesting:
                            index = comment_requested['thread'].index(thread)
                            print(comment_requested['thread'], flush=True)
                            comment_requested['thread'].pop(index)
                            deleted = True
                    
                    if not deleted:
                        return jsonify({'error': 'No comment from this user in this thread'}), 404
                    
                    # Repack object to send
                    for x in comments:
                        if x['commentID'] == data[delete_term]:
                            x = comment_requested['thread']

                    
                    playlist = db.playlists.find_one_and_update(
                        {'playlistName': playlistName},
                        {'$set': {'commentSection': comments}},
                        return_document = ReturnDocument.AFTER
                    )

                else:
                    return jsonify({'error': 'No comment in this thread'}), 404


            if delete_term == 'comment':
                #check if user has comment in playlist at numbered position
                comments = to_delete['commentSection']
                comment_to_delete = next((x for x in comments if x['commentID'] == data[delete_term]), False)
                id_to_delete = comment_to_delete['commentID']
                if comment_to_delete:
                    #check the user creating is the same as the one deleting
                    if comment_to_delete['userEmail'] == userRequesting:
                        index = comments.index(comment_to_delete)
                        comments.pop(index)

                        if not id_to_delete == len(comments):
                            for comment in comments:
                                if comment['commentID'] > id_to_delete:
                                    comment['commentID'] -= 1


                        playlist = db.playlists.find_one_and_update(
                            {'playlistName': playlistName},
                            {'$set': {'commentSection': comments}},
                            return_document = ReturnDocument.AFTER
                        )
                    else:
                        return jsonify({'error': "You cannot delete someone else's comment"}), 403


                else:
                    return jsonify({'error': 'Comment not found'}), 404



        else:
            return jsonify({'error': 'No playlist with that name'}), 404


        print(playlist, flush=True)

        return jsonify(playlist), 200




