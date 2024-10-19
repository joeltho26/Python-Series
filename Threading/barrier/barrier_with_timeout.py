from time import sleep, time
from random import random
from threading import Thread, Barrier, BrokenBarrierError


def task(barrier, number):
    value = random() * 10
    sleep(value)
    print(f'Thread {number} done, got: {value}')
    try:
        barrier.wait(timeout=10)
        #barrier.wait(timeout=10)
    except BrokenBarrierError:
        print(f"thread {number} did not finish on time")

if __name__ == "__main__":
    barrier = Barrier(7 + 1, timeout=10)
    start = time()
    for i in range(7):
        worker = Thread(target=task, args=(barrier, i))
        worker.start()
        
    # wait for all threads to finish
    print('Main thread waiting on all results...')
    try:
        barrier.wait()
        #barrier.wait(timeout=10)
        end = time()
        print(f"Time taken: {start-end}")
        print('All threads have their result')
    except BrokenBarrierError:
        print('Some threads did not finish on time...')