import json

class TestAppRoutes():
    def test_home(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        print(res)
        assert res.data == b'this works'



class TestPlaylistRoutes():
    
    def test_all_playlists(self, api):
        res = api.get('/allplaylists')
        print(res.json)
        assert res.status == '200 OK'
        assert res.json[0]['playlistName'] == 'playlistX'

    def test_create_playlist(self, api):
        res = api.post('/playlist/new', json={
            "email": "gio@gio.com",
            "playlistName": "NewPlsaylist"
            })

        print(res.data)
        assert res.status == '200 OK'        


    


