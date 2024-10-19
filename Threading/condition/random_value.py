from time import sleep
from random import random
from threading import Thread, Condition

# target function
def task(condition, number):
    # wait to be notified
    print(f'Thread {number} waiting...')
    with condition:
        condition.wait()
    # block for a moment
    value = random()
    sleep(value)
    # report a result
    print(f'Thread {number} got {value}')

if __name__ == "__main__":
    # create a condition
    condition = Condition()
    # start a bunch of threads that will wait to be notified
    for i in range(5):
        worker = Thread(target=task, args=(condition, i))
        worker.start()
    # block for a moment
    sleep(1)
    # notify all waiting threads that they can run
    with condition:
        # wait to be notified
        print("proceed with random value...")
        condition.notify_all()
    # block until all non-daemon threads finish...