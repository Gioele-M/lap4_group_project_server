from flask import Flask, jsonify, request
import uuid

class User:

    def signup(self):
        data = request.get_json()
        # print(data, flush=True)
        user = {
            "_id": uuid.uuid4().hex,
            "username": data['username'],
            "userEmail": data['email'],
            "password": data['password']
        }
        return jsonify(user), 200
