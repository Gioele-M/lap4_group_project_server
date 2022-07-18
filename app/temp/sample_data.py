users_model = {
    'username': 'Matteo',
    'hashedPassword': 'notsohashed',
    'userEmail': 'matteo@gmail.com', #primary key
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
            'commentID': 1, #sequential
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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
                'commentID': 1, #sequential
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
                'chapter1': {
                    'chapterTitle': 'first chapter',
                    'video_url': 'https://www.youtube.com/watch?v=7Q17ubqLfaM',
                    'start': '0.00',
                    'end': '0.30',
                    'text': 'This is the section with the notes on the first chapter'
                }

                
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

