db = db.getSiblingDB("wewa");
db.users.drop();

db.users.insertMany([
    {
        "username": 1,
        "name": "Lion",
        "type": "wild"
    },
    {
        "username": 2,
        "name": "Cow",
        "type": "domestic"
    },
    {
        "username": 3,
        "name": "Tiger",
        "type": "wild"
    },
]);
