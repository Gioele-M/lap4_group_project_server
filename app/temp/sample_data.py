users_model = {
    'username': 'Matteo',
    'hashedPassword': 'notsohashed',
    'userEmail': 'matteo@gmail.com',  # primary key
    'token': 'token_string',
    'previousTokens': ['token1', 'token2'],
    'lastSelection': [{'selectedNote': 'chapter1', 'selectedPlaylist': 'playlistName'}],
    'recentPlaylist': [
        'playlist1'
    ],
    'favourites': ['playlistNameX', 'playlistNameY'],
    'achievement': ['badgeX', 'badgeY']
}


playlist_model = {
    'playlistName': 'playlistX',
    'playlistOwner': 'matteo@gmail.com',
    'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
    'public': True,
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
            'commentID': 1,  # sequential
            'timestamp': '00.00.00.10.05.22',
            'username': 'Matteo',
            'userEmail': 'matteo@gmail.com',
            'comment': 'This playlist is great :)',
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
            'chapterId': 1,
            'chapterTitle': 'first chapter',
            'video_url': 'youtube.com',
            'start': '0.00',
            'end': '0.30',
            'text': 'This is the section with the notes on the first chapter'
        }
    ]
}


trending_topics = [
    {
        'playlistName': 'playlistA',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
      "uuid": "c1db11dce02d4088b65b21a43536d8vc",
      'chapterId': 4,
        "chapterTitle": "Remote APIs",
        "start": "12.55",
        "end": "17.03",
        "text": "What is the benefit of using Remote APIs",
        "video_url": "https://www.youtube.com/watch?v=GZvSYJDk-us"
    },

      {
        "uuid": "12db01dce02d4088b65b21a43536d8vc",
        'chapterId': 5,
        "chapterTitle": "Software Testing",
        "start": "03.29",
        "end": "06.00",
        "text": "Software testing is defined as an activity to check whether the actual results match the expected results and to ensure that the software system is defect free.",
        "video_url": "https://www.youtube.com/watch?v=sO8eGL6SFsA"
    },

     {
      "uuid": "c1db01dc202d4088b65b21a43536d8vc",
      'chapterId': 6,
        "chapterTitle": "React",
        "start": "00.57",
        "end": "02.43",
        "text": "What are the essentials that you need to know to start a react app?",
        "video_url": "https://www.youtube.com/watch?v=hQAHSlTtcmY"
    },

         {
          "uuid": "c1db01dc702d4088b65b21a43536d8vc",
          'chapterId': 7,
        "chapterTitle": "Redux",
        "start": "00.17",
        "end": "00.25",
        "text": "Redux is a pattern and library that helps developers implement complex state management requirements at scale",
        "video_url": "https://www.youtube.com/watch?v=_shA5Xwe8_4"
    },
             {
              "uuid": "c1db01dce02d4088b65b21a43536b8vc",
              'chapterId': 8,
        "chapterTitle": "Python Lists",
        "start": "17.40",
        "end": "24.14",
        "text": "Lists are used to store multiple items in a single variable.Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.Lists are created using square brackets",
        "video_url": "https://www.youtube.com/watch?v=JJmcL1N2KQs&t=861s"
    },

             {
              "uuid": "c1db01dce02d4n88b65b21a43536d8vc",
              'chapterId': 9,
        "chapterTitle": "How do I use a Docker Container",
        "start": "7.12",
        "end": "08.51",
        "text": "Docker website with info on docker containers:https://www.docker.com/resources/what-container/",
        "video_url": "https://www.youtube.com/watch?v=gAkwW2tuIqE"
    },

          {
            "uuid": "c1db01dwe02d4088b65b21a43536d8vc",
            'chapterId': 10,
        "chapterTitle": "Flask vs Django",
        "start": "00.00",
        "end": "01.30",
        "text": "Django, on the one hand, is a full-stack web framework, whereas Flask is a light-weight, extensible framework. If you want to dig more into coding and learn core concepts, Flask helps you understand how each component from the back-end works to get a simple web application up and running",
        "video_url": "https://www.youtube.com/watch?v=3vfum74ggHE"
    }
        
    ]
    },
    {
        'playlistName': 'playlistB',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'playlistC',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'playlistD',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'playlistE',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'playlistF',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'playlistG',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'playlistH',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'playlistI',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
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
                'commentID': 1,  # sequential
                'timestamp': '00.00.00.10.05.22',
                'username': 'Matteo',
                'userEmail': 'matteo@gmail.com',
                'comment': 'This playlist is great :)',
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
                'chapterId': 1,
                'chapterTitle': 'first chapter',
                'video_url': 'youtube.com',
                'start': '0.00',
                'end': '0.30',
                'text': 'This is the section with the notes on the first chapter'
            }
        ]
    },
    {
        'playlistName': 'empty playlist',
        'playlistOwner': 'matteo@gmail.com',
        'editingAccess': ['gioele@gmail.com', 'igor@gmail.com'],
        'public': True,
        'playlistTheme': '(0,0,0)',
        'tags': ['tag1', 'tag2'],
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


# result = db.users.insert_many(([
#     {
#         "username": 'Matteo',
#         "userEmail": "matteo@gmail.com",
#         "password": "pass"
#     },
#     {
#         "username": 'Gio',
#         "name": "gio@gmail.com",
#         "password": "pass"
#     },
#     {
#         "username": 'Igor',
#         "name": "igor@gmail.com",
#         "password": "pass"
#     },
# ]))
