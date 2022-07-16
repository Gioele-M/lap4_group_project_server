db = db.getSiblingDB("wewa");
db.users.drop();

db.users.insertMany([
    {
        "_id": "c1db01dce06d4088b65b21a43536d81c",
        "password": "$pbkdf2-sha256$29000$yLm3Viol5BzDuDeGMIbQGg$rFspp6mcmzFZHx/DCymzmqHztJjMcWknCplf6W0KFUc",
        "userEmail": "gio@gio.com",
        "username": "Gio"
    },
    {
        "_id": "7872916045974f82a3b51dd8ae9eece1",
        "password": "$pbkdf2-sha256$29000$l1Lqfa/1nvP.f.9dqzVmLA$bReC2CgBmAoZNHm8TlzNd.6Q7CaN1ky6TUTqWvcrxH8",
        "userEmail": "matteo@gmail.com",
        "username": "Matteo"
    },
    {
        "_id": "d75f3dac482e4eb19cd7ff92cdf3dc84",
        "password": "$pbkdf2-sha256$29000$3hvDWIvRupdyjjGm1Pr/fw$dW2llVMNWBtX2QxMTzF9z7bzsYvEGYEC.rEdSZdyEmI",
        "userEmail": "igor@gmail.com",
        "username": "Igor"
    },
]);
