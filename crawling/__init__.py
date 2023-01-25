from pymongo import MongoClient

if __name__ == "__main__":
    mongo_clust0 = 'mongodb+srv://gon:2025@cluster0.sm3ik1j.mongodb.net/?retryWrites=true&w=majority' # for using cloud
    client = MongoClient(mongo_clust0)
    db = client['myweb'].board

    a = db.find_one({'email': 'y2gon2@gmail.com'})
    print(a)

