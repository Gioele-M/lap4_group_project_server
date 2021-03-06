from crypt import methods
from flask import Flask
from app import app
from models.playlist.models import Playlist

#Non protected
@app.route('/allplaylists')
def get_all():
    return Playlist().showall()

#Non protected
@app.route('/playlist/trending')
def trending():
    return Playlist().showtrending()


#POST
@app.route('/playlist/new', methods=['POST'])
def new_playlist():
    return Playlist().create_playlist()


#Non protected
#"GET"
@app.route('/playlist/search', methods=['POST'])
def get_by_name():
    return Playlist().search_by()



#Patch requiring the userRequesting 
@app.route('/playlist/patch', methods=['PATCH'])
def patch():
    return Playlist().patch()

#patch for everyone
@app.route('/playlist/patchall', methods=['PATCH'])
def patchall():
    return Playlist().patch_all()


#Delete with userRequesting
@app.route('/playlist/delete', methods=['DELETE'])
def delete():
    return Playlist().delete_auth()

@app.route('/playlist/deleteall', methods=['DELETE'])
def deleteall():
    return Playlist().delete_for_all()
