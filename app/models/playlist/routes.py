from crypt import methods
from flask import Flask
from app import app, token_required
from models.playlist.models import Playlist


@app.route('/allplaylists')
def get_all():
    return Playlist().showall()

#POST
@app.route('/playlist/new', methods=['POST'])
def new_playlist():
    return Playlist().create_playlist()


#"GET"
@app.route('/playlist/search', methods=['POST'])
def get_by_name():
    return Playlist().search_by()



#Patch
@app.route('/playlist/patch', methods=['PATCH'])
def patch():
    return Playlist().patch()
