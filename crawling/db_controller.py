from pymongo import MongoClient

def get_all(db):
    return db.find()