import json


class TestAppRoutes():
    def test_home(self, api):
        res = api.get('/')
        assert res.status == '200 OK'
        # print(res)
        assert res.data == b'this works'


class TestUserRoutes():

    def test_signup(self, api):
        res = api.post('/user/signup', json={
            'username': 'string',
            'password': 'string',
            'email': 'string@gmail.com'
        })
        assert res.status == '200 OK'
        assert b'string@gmail.com' in res.data

    def test_fail_signup(self, api):
        res = api.post('/user/signup', json={
            'username': 'string',
            'password': 'string',
            'email': 'string@gmail.com'
        })
        assert res.status == '406 NOT ACCEPTABLE'
        assert b'Email address already in use' in res.data

    def test_login(self, api):
        res = api.post('/user/login', json={
            'email': 'string@gmail.com',
            'password': 'string'
        })
        print(res.data)
        assert res.status == '200 OK'
        assert b'"userEmail": "string@gmail.com"' in res.data

    def test_fail_login(self, api):
        res = api.post('/user/login', json={
            'email': 'string@gmail.com',
            'password': 'wrong'
        })
        print(res.data)
        assert res.status == '401 UNAUTHORIZED'
        assert b'Invalid login credentials' in res.data

    def test_patch_favourites_add(self, api):
        res = api.patch('/user/favourites', json={
            "email": "string@gmail.com",
            "token": "xxx",
            "favourite": "newsport",
            "action": "add"
        })
        print(res.data)
        assert res.status == '200 OK'
        assert b'"username": "string"' in res.data

    def test_fail_patch_favourites_add(self, api):
        res = api.patch('/user/favourites', json={
            "email": "string@gmail.com",
            "token": "xxx",
            "favourite": "newsport",
            "action": "add"
        })
        print(res.data)
        assert res.status == '406 NOT ACCEPTABLE'
        assert b'This is in favourites already' in res.data

    def test_patch_favourites_remove(self, api):
        res = api.patch('/user/favourites', json={
            "email": "string@gmail.com",
            "token": "xxx",
            "favourite": "newsport",
            "action": "remove"
        })
        print(res.data)
        assert res.status == '200 OK'
        assert b'"username": "string"' in res.data

    def test_fail_patch_favourites_remove(self, api):
        res = api.patch('/user/favourites', json={
            "email": "string@gmail.com",
            "token": "xxx",
            "favourite": "newsport",
            "action": "remove"
        })
        print(res.data)
        assert res.status == '406 NOT ACCEPTABLE'
        assert b'This was not in favourites' in res.data


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
        # print(res.data)
        assert res.status == '200 OK'
        assert b'NewPlaylist' in res.data

    def test_search_playlist_by_owner(self, api):
        res = api.post('/playlist/search', json={
            "playlistOwner": 'gio@gio.com'
        })
        # print(res.data)
        assert res.status == '200 OK'
        assert b'NewPlaylist' in res.data

    def test_search_playlist_by_tags(self, api):
        res = api.post('/playlist/search', json={
            "tags": 'tag1'
        })
        # print(res.data)
        assert res.status == '200 OK'
        assert b'igor@gmail.com' in res.data

    def test_fail_search_playlist(self, api):
        res = api.post('/playlist/search', json={
            "playlistNam": ''
        })
        assert b'Playlist not found' in res.data
        assert res.status == '404 NOT FOUND'

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

    def test_patch_theme(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "React",
            "playlistTheme": "(0,0,0)",
            "token": "xxx"
        })
        assert res.status == '200 OK'
        assert b'Redux' in res.data

    def test_patch_editaccess(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "React",
            "editingAccess": "newemail",
            "token": "xxx"
        })
        assert res.status == '200 OK'
        assert b'Redux' in res.data

    def test_patch_edit_tags(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "React",
            "tags": "trytag",
            "token": "xxx"
        })
        assert res.status == '200 OK'
        assert b'Redux' in res.data

    def test_patch_edit_public(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "React",
            "public": "False",
            "token": "xxx"
        })
        assert res.status == '200 OK'
        assert b'Redux' in res.data

    def test_fail_patch_playlist(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "Redux",
            "newName": "React",
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '401 UNAUTHORIZED'
        assert b'No playlist with that name' in res.data

    def test_patch_add_chapter(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "React",
            "chapters": {
                'uuid': 'xxx',
                "chapterId": 4,
                "chapterTitle": "firdsst c",
                "end": "0.30",
                "start": "0.00",
                "text": "This is the section with the notes on the first chapter",
                "video_url": "youtube.com"
            },
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '200 OK'
        assert b"matteo@gmail.com" in res.data

    def test_patch_chapter(self, api):
        res = api.patch('/playlist/patch', json={
            "userRequesting": "matteo@gmail.com",
            "playlistName": "React",
            "chapters": {
                "chapterId": 2,
                "chapterTitle": "firdsst c",
                "end": "0.30",
                "start": "0.00",
                "text": "This is the section with",
                "video_url": "youtube.com"
            },
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '200 OK'
        assert b"matteo@gmail.com" in res.data

    def test_patch_ratings(self, api):
        res = api.patch('/playlist/patchall', json={
            "userRequesting": "gioele@gmail.com",
            "playlistName": "React",
            "userStars": 3,
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '200 OK'
        assert b"gioele@gmail.com" in res.data

    def test_fail_patch_ratings(self, api):
        res = api.patch('/playlist/patchall', json={
            "userRequesting": "gioele@gmail.com",
            "playlistName": "Reactw",
            "userStars": 3,
            "token": "xxx"
        })
        # print(res.data)
        assert res.status == '406 NOT ACCEPTABLE'
        assert b'No playlist with that name' in res.data

    def test_patch_comment(self, api):
        res = api.patch('/playlist/patchall', json={
            "userRequesting": "gioele@gmail.com",
            "playlistName": "Build a website with HTML-CSS-JS",
            "commentSection": {
                "comment": "This playlist is great!",
                "commentID": 1,
                "thread": [
                    {
                        "reply": "great indeed!",
                        "timestamp": "00.00.00.10.05.22",
                        "userEmail": "gioele@gmail.com",
                        "username": "Gio"
                    }
                ],
                "timestamp": "00.00.00.10.05.22",
                "userEmail": "matteo@gmail.com",
                "username": "Matteo"
            },
            "token": "xxx"
        })
        assert res.status == '200 OK'
        assert b'gioele@gmail.com' in res.data

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
        # print(res.data)
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
