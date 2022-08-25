import pymongo
client = pymongo.MongoClient("mongodb+srv://omkartiwari2333:Omkartiwari23031999@cluster0.3pxod5c.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d= {
    "name": "omkar",
    "email": "omkartiwari2333@gmail.com",
    "surname": "tiwari"
}
d= {
    "name": "omkar",
    "email": "omkartiwari2333@gmail.com",
    "surname": "tiwari"
}
d= {
    "name": "omkar",
    "email": "omkartiwari2333@gmail.com",
    "surname": "tiwari"
}
db1 = client['mongotest']
coll = db1["test"]
coll.insert_one(d)
