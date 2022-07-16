from re import T
from flask import Flask, jsonify, request, session
import uuid
from passlib.hash import pbkdf2_sha256
from app import db

class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200


    #signup user
    def signup(self):
        print('getting in', flush=True)
        print(request, flush=True)
        
        data = request.get_json()
        # except Exception as e:
        #     print(e, flush=True)
            

        print(data, flush=True)
        user = {
            "_id": uuid.uuid4().hex,
            "username": data['username'],
            "userEmail": data['email'],
            "password": data['password']
        }

        #password encription
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        #handle double emails
        if db.users.find_one({'userEmail': user['userEmail']}):
            return jsonify({'error': 'Email address already in use'}), 406
        
        #add user to db
        if db.users.insert_one(user):
            return self.start_session(user)

        #if any other issue
        return jsonify({ 'error': 'Signup failed'}), 400



    def login(self):
        data = request.get_json()
        user = db.users.find_one({
            'userEmail':  data['email']
        })

        if user and pbkdf2_sha256.verify(data['password'], user['password']):
            return self.start_session(user)

        return jsonify({'error': 'Invalid login credentials'}), 401


    def signout(self):
        session.clear()
        return jsonify({'message': 'signed out'})
