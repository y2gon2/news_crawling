import schedule
import time

def message(a):
    return a + 1

a = 1
result = schedule.every(1).seconds.do(message, a)

while True:
    print(result)
    schedule.run_pending()
    time.sleep(5)