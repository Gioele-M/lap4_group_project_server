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
        # print(res.json)
        assert res.status == '200 OK'
        assert 'HTML-CSS-JS' in res.json[0]['playlistName']

    def test_trending(self, api):
        res = api.get('playlist/trending')
        # print(res.json)
        assert res.status == '200 OK'
        assert b'b49a866d572d45f0bed20c43ea40884c' in res.data

    def test_create_playlist(self, api):
        res = api.post('/playlist/new', json={
            "email": "gio@gio.com",
            "playlistName": "NewPlaylist"
        })
        # print(res.data)
        assert res.status == '200 OK'
        assert b'NewPlaylist' in res.data

    def test_fail_create_playlist(self, api):
        res = api.post('/playlist/new', json={
            "email": "gio@gio.com",
            "playlistName": "NewPlaylist"
        })
        assert res.status == '406 NOT ACCEPTABLE'
        assert b'Playlist name already taken' in res.data


    def test_search_playlist(self, api):
        res = api.post('/playlist/search', json={
            "playlistName": 'NewPlaylist'
        })
        print(res.data)
        assert res.status == '200 OK'
        assert b'NewPlaylist' in res.data


    def test_fail_search_playlist(self, api):
        res = api.post('/playlist/search', json={
            "playlistName": ''
        })
        assert b'[]' in res.data

    def test_patch_playlist(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "React",
            "newName": "Redux",
            "token": "xxx"
        })
        api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "Redux",
            "newName": "React",
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '200 OK'
        assert b'Redux' in res.data


    def test_fail_patch_playlist(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "Redux",
            "newName": "React",
            "token": "xxx"
        })
        print(res.data)
        assert res.status == '401 UNAUTHORIZED'
        assert b'No playlist with that name' in res.data


    def test_patch_ratings(self, api):
        res = api.patch('/playlist/patchall', json={
            "userRequesting": "gioele@gmail.com",
            "playlistName": "React",
            "userStars": 3,
            "token": "xxx"
        })
        print(res.data)
        assert res.status == '200 OK'
        assert b"gioele@gmail.com" in res.data


    def test_fail_patch_ratings(self, api):
        res = api.patch('/playlist/patchall', json={
            "userRequesting": "gioele@gmail.com",
            "playlistName": "Reactw",
            "userStars": 3,
            "token": "xxx"
        })
        print(res.data)
        assert res.status == '406 NOT ACCEPTABLE'
        assert b'No playlist with that name' in res.data


    def test_delete_playlist(self, api):
        res = api.delete('/playlist/delete', json={
            "userRequesting": "gio@gio.com",
            "playlistName": "NewPlaylist",
            "playlist": "True",
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '202 ACCEPTED'
        assert b"Playlist deleted" in res.data

    def test_fail_delete_playlist(self, api):
        res = api.delete('/playlist/delete', json={
            "userRequesting": "gio@gio.com",
            "playlistName": "NewPlaylist",
            "playlist": "True",
            "token": "xxx"
        })
        print(res.data)
        assert res.status == '404 NOT FOUND'
        assert b"No playlist with that name" in res.data



    def test_delete_ratings(self, api):
        res = api.delete('/playlist/deleteall', json={
            "userRequesting": "gioele@gmail.com",
            "playlistName": "playlistX",
            "comment": 1,
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '404 NOT FOUND'




