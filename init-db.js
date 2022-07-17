db = db.getSiblingDB("wewa");
db.users.drop();

db.users.insertMany([
    {
        "_id": "c1db01dce06d4088b65b21a43536d81c",
        "password": "$pbkdf2-sha256$29000$yLm3Viol5BzDuDeGMIbQGg$rFspp6mcmzFZHx/DCymzmqHztJjMcWknCplf6W0KFUc",
        "userEmail": "gio@gio.com",
        "username": "Gio",
        "achievement": [
        ],
        "favourites": [
      
        ],
        "lastSelection": {
          "selectedNote": "",
          "selectedPlaylist": ""
        },
        "recentPlaylist": [
      
        ],
        "token": ""
    },
    {
        "_id": "7872916045974f82a3b51dd8ae9eece1",
        "password": "$pbkdf2-sha256$29000$l1Lqfa/1nvP.f.9dqzVmLA$bReC2CgBmAoZNHm8TlzNd.6Q7CaN1ky6TUTqWvcrxH8",
        "userEmail": "matteo@gmail.com",
        "username": "Matteo",
        "achievement": [
        ],
        "favourites": [
      
        ],
        "lastSelection": {
          "selectedNote": "",
          "selectedPlaylist": ""
        },
        "recentPlaylist": [
      
        ],
        "token": ""
    },
    {
        "_id": "d75f3dac482e4eb19cd7ff92cdf3dc84",
        "password": "$pbkdf2-sha256$29000$3hvDWIvRupdyjjGm1Pr/fw$dW2llVMNWBtX2QxMTzF9z7bzsYvEGYEC.rEdSZdyEmI",
        "userEmail": "igor@gmail.com",
        "username": "Igor",
        "achievement": [
        ],
        "favourites": [
      
        ],
        "lastSelection": {
          "selectedNote": "",
          "selectedPlaylist": ""
        },
        "recentPlaylist": [
      
        ],
        "token": ""
    },
]);



db.playlists.drop();


db.playlists.insertMany(
  [{
    "_id": "b49a866d572d45f0bed20c43ea40884c",
    'playlistName': 'playlistX',
    'playlistOwner': 'matteo@gmail.com',
    'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
    'public': 'True',
    'playlistTheme': '(0,0,0)',
    'tags': ['tag1', 'tag2'],
    'averageStars': {
        'currentRating': 3.5,
        'totalStars': 7,
        'totalRatings': 2
    },
    'userStars': [
        {'userEmail': 'gioele@gmail.com', 'rating': 4},
        {'userEmail': 'igor@gmail.com', 'rating': 3}
    ],
    'commentSection': [
        {
            'commentID': 1, 
            'timestamp': '00.00.00.10.05.22',
            'username': 'Matteo',
            'userEmail': 'matteo@gmail.com',
            'comment': 'This playlist is great!',
            'thread': [
                {
                    'timestamp': '00.00.00.10.05.22',
                    'username': 'Gio',
                    'userEmail': 'gioele@gmail.com',
                    'reply': 'great indeed!'
                },
                {   
                    'timestamp': '00.00.00.10.05.22',
                    'username': 'Igor',
                    'userEmail': 'igor@gmail.com',
                    'reply': 'Looks great but I would add another section!'
                }
            ]
        }
    ],
    'chapters': [
        {
            'chapter1': {
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }            
        }
    ]
  }
  ,
  {
    "_id": "b49a866d572d45f0bed20c43ea40884a",
    'playlistName': 'playlistY',
    'playlistOwner': 'gio@gio.com',
    'editingAccess': [],
    'public': 'True',
    'playlistTheme': '(0,0,0)',
    'tags': ['tag1', 'tag2'],
    'averageStars': {
        'currentRating': 3,
        'totalStars': 6,
        'totalRatings': 2
    },
    'userStars': [
        {'userEmail': 'gioele@gmail.com', 'rating': 4},
        {'userEmail': 'igor@gmail.com', 'rating': 2}
    ],
    'commentSection': [
        {
            'commentID': 1,
            'timestamp': '00.00.00.10.05.22',
            'username': 'Matteo',
            'userEmail': 'matteo@gmail.com',
            'comment': 'This playlist is not amazing really',
            'thread': [
                {
                    'timestamp': '00.00.00.10.05.22',
                    'username': 'Gio',
                    'userEmail': 'gioele@gmail.com',
                    'reply': 'sucks indeed!'
                },
                {   
                    'timestamp': '00.00.00.10.05.22',
                    'username': 'Igor',
                    'userEmail': 'igor@gmail.com',
                    'reply': 'Looks great but I would add another section!'
                }
            ]
        }
    ],
    'chapters': [
        {
            'chapter1': {
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            } 
        }
    ]
  }
  ,
  {
    "_id": "b49a866d572d45f0bed20c43ea40884b",
    'playlistName': 'emptyPlaylist',
    'playlistOwner': 'igor@gmail.com',
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
  ]
);







