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
                'chapterId': 1,
                'chapterTitle': 'Why containers are useful',
                'video_url': 'https://www.youtube.com/watch?v=_dfLOzuIg2o',
                'start': '0.00',
                'end': '1.30',
                'text': "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
            },
            {
                'chapterId': 2,
                'chapterTitle': 'Introduction to containers',
                'video_url': 'https://www.youtube.com/watch?v=cjXI-yxqGTI',
                'start': '1.00',
                'end': '4.30',
                'text': 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
            },
            {
                'chapterId': 3,
                'chapterTitle': 'Second part of containers',
                'video_url': 'https://www.youtube.com/watch?v=pxwUXJmAER4',
                'start': '5.00',
                'end': '8.30',
                'text': "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
            },
            {
                'chapterId': 4,
                'chapterTitle': 'Introduction to docker',
                'video_url': 'https://www.youtube.com/watch?v=eGz9DS-aIeY',
                'start': '1.00',
                'end': '4.30',
                'text': 'The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.'
            },
            {
                'chapterId': 5,
                'chapterTitle': 'Usage of docker',
                'video_url': 'https://www.youtube.com/watch?v=XCWWPpfdbsM',
                'start': '0.00',
                'end': '3.30',
                'text': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text."
            },
            {
                'chapterId': 6,
                'chapterTitle': 'Conclusions',
                'video_url': 'https://www.youtube.com/watch?v=mRMmlo_Uqcs',
                'start': '5.00',
                'end': '6.30',
                'text': 'All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.'
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
