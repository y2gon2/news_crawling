from pymongo import MongoClient
from db_controller import get_all
from webdriver_controller import run_webdriver
from file_controller import save
from mailing import send


def news_crawling(db):
    data = get_all(db)

    for per_email in data:
        email = per_email['email']
        words = per_email['words']

        for keyword in words:
            result = run_webdriver(keyword)
            save(email, result)
            send(email, result['date'], result['keyword'])

if __name__ == "__main__":
    mongo_clust0 = 'mongodb+srv://gon:2025@cluster0.sm3ik1j.mongodb.net/?retryWrites=true&w=majority' # for using cloud

    client = MongoClient(mongo_clust0)
    db = client['myweb'].board

    news_crawling(db)
