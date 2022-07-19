from flask import Flask, jsonify, request, session
import uuid
from passlib.hash import pbkdf2_sha256
from pymongo import ReturnDocument
import jwt
import datetime
from app import app, db, token_required


class User:

    # def start_session(self, user):
    #     del user['password']
    #     session['logged_in'] = True
    #     session['user'] = user
    #     return jsonify(user), 200

    def send_token(self, user):  
        del user['password']
        #Token expires in 3h
        token = jwt.encode({'user': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=3)}, app.config['SECRET_KEY'])
        user['token'] = token#.decode('UTF-8')
        return jsonify(user), 200



    #signup user
    def signup(self):
        
        data = request.get_json()
        # except Exception as e:
        #     print(e, flush=True)
            

        print(data, flush=True)
        user = {
            "_id": uuid.uuid4().hex,
            "username": data['username'],
            "userEmail": data['email'],
            "password": data['password'],
            "token": "",
            'lastSelection': {'selectedNote': '', 'selectedPlaylist': ''},
            'recentPlaylist': [],
            'favourites': [],
            'achievement': []
        }

        #password encription
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        #handle double emails
        if db.users.find_one({'userEmail': user['userEmail']}):
            return jsonify({'error': 'Email address already in use'}), 406
        
        #add user to db
        if db.users.insert_one(user):
            return self.send_token(user)

        #if any other issue
        return jsonify({ 'error': 'Signup failed'}), 400



    def login(self):
        data = request.get_json()
        user = db.users.find_one({
            'userEmail':  data['email']
        })

        if user and pbkdf2_sha256.verify(data['password'], user['password']):
            # return self.start_session(user)
            return self.send_token(user)

        return jsonify({'error': 'Invalid login credentials'}), 401


    # def signout(self):
    #     session.clear()
    #     return jsonify({'message': 'signed out'})

    @token_required
    def update_favourites(self):
        data = request.get_json()
        new_fav = data['favourite']
        action = data['action']
        _user = db.users.find_one({
            'userEmail':  data['email']
        })

        if action == 'add':
            if new_fav in _user['favourites']:
                return jsonify({ "error": "This is in favourites already" }), 406

            _user['favourites'].append(new_fav)
            user = db.users.find_one_and_update(
                {'userEmail':  data['email']},
                {"$set": {"favourites": _user['favourites']}},
                return_document = ReturnDocument.AFTER

            )

        elif action == 'remove':
            if new_fav not in _user['favourites']:
                return jsonify({ "error": "This was not in favourites" }), 406

            _user['favourites'].remove(new_fav)
            user = db.users.find_one_and_update(
                {'userEmail':  data['email']},
                {"$set": {"favourites": _user['favourites']}},
                return_document = ReturnDocument.AFTER
            )

        else:
            return jsonify({'error': 'Action invalid'}), 405        


        return jsonify(user)



