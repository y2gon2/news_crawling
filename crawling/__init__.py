from pymongo import MongoClient
# from db_controller import get_database
from webdriver_controller import run_webdriver
from file_controller import save
from mailing import send
# from multiprocessing import Pool, Process, Queue
# import schedule  # .. 해당 lib 로 실행한 함수의 return 값을 어떻게 받는지 모르겠음..
from threading import Thread
from queue import Queue
import time

MONGO_CLUST0 = 'mongodb+srv://gon:2025@cluster0.sm3ik1j.mongodb.net/?retryWrites=true&w=majority' # for using cloud
CLIENT = MongoClient(MONGO_CLUST0)
DB = CLIENT['myweb'].board

def get_database(local_time):
    data = DB.find_one(   # find_one 만 사용하면 안되는데.. ;;; 왜 find 는 안먹히지;;;
        {"time": local_time}
    )
    if data == None:
        return 0
    else:
        return data

def news_crawling(queue):
    print('news_crawling thread is started!')
    while True:
        data = queue.get()
        print(data)
        email = data['email']
        words = data['words']

        for keyword in words:
            result = run_webdriver(keyword)
            save(email, result)
            send(email, result['date'], result['keyword'])

        time.sleep(1)

def poll_db(queue):
    print('poll_db thread is started!')
    next_min = int(time.strftime('%M', time.localtime(time.time())))
    while True:
        cur_min = int(time.strftime('%M', time.localtime(time.time())))
        local_time = time.strftime('%H:%M', time.localtime(time.time()))

        if next_min == cur_min:
            print('%s : time to poll!!' % local_time)
            data = get_database(local_time)
            if data != 0:
                queue.put(data)
            if cur_min == 59:
                next_min = 0
            else:
                next_min += 1

        time.sleep(1)


if __name__ == "__main__":
    queue = Queue()
    polling_thread = Thread(target=poll_db, args=(queue, ))
    crawling_thread = Thread(target=news_crawling, args=(queue, ))
    polling_thread.start()
    crawling_thread.start()
    polling_thread.join()
    crawling_thread.join()

    # polling_p = Process(target=poll_db, args=(queue, ))
    # crawling_p = Process(target=news_crawling, args=(queue, )) # process pool 로 작업 해야 할거 같은데.. 잘 모르니까 우선 단일 process 로.

    # polling_p.start()
    # crawling_p.start()
    #
    # polling_p.join()
    # crawling_p.join()

