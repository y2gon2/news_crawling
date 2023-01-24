from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")

    db = client['test-db']
    # print(client.list_database_names())

    data = {
        "author": "han",
        "text": "mongoDB is what??",
        "tags": ["mong", "python", "hell"]
    }

    db['posts11'].insert_one(
        {'author': 'Lee', 'address': 'Busan'}
    )

    db['posts'].delete_many({})




