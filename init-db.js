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
    'playlistName': 'Build a website with HTML-CSS-JS',
    'playlistOwner': 'matteo@gmail.com',
    'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
    'public': 'True',
    'playlistTheme': '(0,0,0)',
    'tags': ['tag1', 'tag2'],
    'averageStars': {
        'currentRating': 4.5,
        'totalStars': 9,
        'totalRatings': 2
    },
    'userStars': [
        {'userEmail': 'gioele@gmail.com', 'rating': 4},
        {'userEmail': 'igor@gmail.com', 'rating': 5}
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
        "uuid": "c1db01dce06d4088b65b21as3536d81c",
        'chapterId': 1,
        "chapterTitle": "HTML tags",
        "start": "20.24",
        "end": "25.40",
        "text": "What are some basic HTML (HyperText Markup Language) tags and how do you start writing HTML",
        "video_url": "https://www.youtube.com/watch?v=qz0aGYrrlhU"
    },

    {
      "uuid": "c1db01dce02d4088b65b21a43536d81c",
      'chapterId': 2,
        "chapterTitle": "What is CSS",
        "start": "00.25",
        "end": "01.15",
        "text": "HTML (the Hypertext Markup Language) and CSS (Cascading Style Sheets) are two of the core technologies for building Web pages. HTML provides the structure of the page, CSS the (visual and aural) layout, for a variety of devices.",
        "video_url": "https://www.youtube.com/watch?v=1PnVor36_40"
    },

    {
      "uuid": "c1db01dce02d4088b65b21a43536d8vc",
      'chapterId': 3,
        "chapterTitle": "Javascript Summary",
        "start": "00.00",
        "end": "02.35",
        "text": "JavaScript is the the programming language that built the web. Learn how it evolved into a powerful tool for building websites, servers with Node.js, mobile apps, desktop software, and more.",
        "video_url": "https://www.youtube.com/watch?v=DHjqpvDnNGE"
    },
    {
        "uuid": "c1dg01dce02d4088b65b21a43536b8vc",
        'chapterId': 4,
        "chapterTitle": "JavaScript in the web",
        "start": "17.40",
        "end": "24.14",
        "text": "Lists are used to store multiple items in a single variable.Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.Lists are created using square brackets",
        "video_url": "https://www.youtube.com/watch?v=XnJ4K7nm_5A"
    }  
    ]
  },
  {
    "_id": "b49a866d572d45f0bed20c43aa40884b",
    'playlistName': 'React',
    'playlistOwner': 'matteo@gmail.com',
    'editingAccess': [],
    'public': 'True',
    'playlistTheme': '(0,0,0)',
    'tags': [],
    'averageStars': {
        'currentRating': 4,
        'totalStars': 8,
        'totalRatings': 2
    },
    'userStars': [],
    'commentSection': [],
    'chapters': [
      {
        "uuid": "c1db01dce02e4n88b65b21a43536d8vc",
        'chapterId': 1,
        "chapterTitle": "How do I use a Docker Container",
        "start": "7.12",
        "end": "08.51",
        "text": "Docker website with info on docker containers:https://www.docker.com/resources/what-container/",
        "video_url": "https://www.youtube.com/watch?v=gAkwW2tuIqE"
    },
      {
      "uuid": "c1db01dc202d4088b65b21a43536d8vc",
      'chapterId': 2,
        "chapterTitle": "React",
        "start": "00.57",
        "end": "02.43",
        "text": "What are the essentials that you need to know to start a react app?",
        "video_url": "https://www.youtube.com/watch?v=hQAHSlTtcmY"
    },

    {
      "uuid": "c1db01dc702d4088b65b21a43536d8vc",
        'chapterId': 3,
        "chapterTitle": "Redux",
        "start": "00.17",
        "end": "00.25",
        "text": "Redux is a pattern and library that helps developers implement complex state management requirements at scale",
        "video_url": "https://www.youtube.com/watch?v=_shA5Xwe8_4"
    }
    ]
  }
  ,
  {
    "_id": "b49a866d572d45f0bed20s43ea40884b",
    'playlistName': 'Python',
    'playlistOwner': 'gio@gmail.com',
    'editingAccess': ['matteo@gmail.com'],
    'public': 'True',
    'playlistTheme': '(0,0,0)',
    'tags': [],
    'averageStars': {
        'currentRating': 2.5,
        'totalStars': 5,
        'totalRatings': 2
    },
    'userStars': [],
    'commentSection': [],
    'chapters': [
    {
              "uuid": "c1db01dce02d4088b65b21a43536b8vc",
              'chapterId': 1,
        "chapterTitle": "Python Lists",
        "start": "17.40",
        "end": "24.14",
        "text": "Lists are used to store multiple items in a single variable.Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.Lists are created using square brackets",
        "video_url": "https://www.youtube.com/watch?v=JJmcL1N2KQs&t=861s"
    },
    {
              "uuid": "c1db01dce02d4088b65b21a43636b8vc",
              'chapterId': 2,
        "chapterTitle": "Things to add",
        "start": "17.40",
        "end": "24.14",
        "text": "Need to add loops, dictionaries, variables and all the OOP references!",
        "video_url": ""
    }
  ]
  }
  ,
  {
    "_id": "b49a866d572d45f0bed20c43ea40884a",
    'playlistName': 'Building APIs',
    'playlistOwner': 'matteo@gmail.com',
    'editingAccess': [],
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
        {'userEmail': 'igor@gmail.com', 'rating': 2}
    ],
    'commentSection': [
        
    ],
    'chapters': [
          {
      "uuid": "c1db11dce02d4088b65b21a43536d8vc",
      'chapterId': 1,
        "chapterTitle": "Remote APIs",
        "start": "12.55",
        "end": "17.03",
        "text": "What is the benefit of using Remote APIs",
        "video_url": "https://www.youtube.com/watch?v=GZvSYJDk-us"
    },
        {
        "uuid": "c1db01dce02d4n88b65b21a43536d8vc",
        'chapterId': 2,
        "chapterTitle": "How do I use a Docker Container",
        "start": "7.12",
        "end": "08.51",
        "text": "Docker website with info on docker containers:https://www.docker.com/resources/what-container/",
        "video_url": "https://www.youtube.com/watch?v=gAkwW2tuIqE"
    },
              {
        "uuid": "12db01dce02d4088b65b21a43536d8vc",
        'chapterId': 3,
        "chapterTitle": "Software Testing",
        "start": "03.29",
        "end": "06.00",
        "text": "Software testing is defined as an activity to check whether the actual results match the expected results and to ensure that the software system is defect free.",
        "video_url": "https://www.youtube.com/watch?v=sO8eGL6SFsA"
    },
              {
            "uuid": "c1db01dwe02d4088b65b21a43536d8vc",
            'chapterId': 4,
        "chapterTitle": "Flask vs Django",
        "start": "00.00",
        "end": "01.30",
        "text": "Django, on the one hand, is a full-stack web framework, whereas Flask is a light-weight, extensible framework. If you want to dig more into coding and learn core concepts, Flask helps you understand how each component from the back-end works to get a simple web application up and running",
        "video_url": "https://www.youtube.com/watch?v=3vfum74ggHE"
    }    

  
    ]
  }
  ,
  {
    "_id": "b49a866d572d45f0bed20c43ea40884b",
    'playlistName': 'Things to check out',
    'playlistOwner': 'igor@gmail.com',
    'editingAccess': [],
    'public': 'True',
    'playlistTheme': '(0,0,0)',
    'tags': [],
    'averageStars': {
        'currentRating': 2,
        'totalStars': 4,
        'totalRatings': 2
    },
    'userStars': [],
    'commentSection': [],
    'chapters': [
    {
        "uuid": "c15b01dce06d4088b65b21as3536d81c",
        'chapterId': 1,
        "chapterTitle": "Learn French",
        "start": "00.25",
        "end": "15.08",
        "text": "If I wanted to introduce myself in French, what would I say? ",
        "video_url": "https://www.youtube.com/watch?v=9JZ5hgRJac4"
},
{
        "uuid": "c14b01dce06d4088b65b21as3536d81c",
        'chapterId': 2,
        "chapterTitle": "Space - Mars",
        "start": "00.25",
        "end": "25.40",
        "text": "Scientists and engineers involved in the ExoMars 2020 program discuss the latest on the search for life on Mars.",
        "video_url": "https://www.youtube.com/watch?v=GHm8VKhI6i4"
},
{
        "uuid": "c1db01dce06d9088b65b21as3536d81c",
        'chapterId': 3,
       "chapterTitle": "Love this Fendi Fashion Show Collection",
        "start": "01.10",
        "end": "01.48",
        "text": "This is the #FendiCouture Autumn Winter 2022 collection, very inspiring! Love it! ",
        "video_url": "https://www.youtube.com/watch?v=jijn7a2ZHFE"
},
{
        "uuid": "c1db91dce06d4088b65b21as3536d81c",
        'chapterId': 4,
        "chapterTitle": "Best Games in 2019",
        "start": "07.00",
        "end": "07.38",
        "text": "For research purposes, these searches are found by using data from multiple sites and they might be a little off from actual values. Definitely interesting to see the results",
        "video_url": "https://www.youtube.com/watch?v=rU19OFZ0vz4"
}


]
  }
  ]
);







