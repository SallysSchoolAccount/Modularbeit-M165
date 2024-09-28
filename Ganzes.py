import pymongo

verbindung = pymongo.MongoClient("mongodb://localhost:27017/")
datenbank = verbindung["Spiele"]
collection = datenbank["Spielsammlung"]

for x in collection.find({}, {"_id": 1, "name": 1, "jahr": 1}):
    print(x)