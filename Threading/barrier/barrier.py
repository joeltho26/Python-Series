from time import sleep
from random import random
from threading import Thread, Barrier

def task(barrier, number):

    value = random() * 10
    sleep(value)
    print(f'Thread {number} done, got: {value}')
    
    # wait on all other threads to complete
    barrier.wait()
    
if __name__ == "__main__":
    barrier = Barrier(5 + 1)
    no_of_threads = 5
    for i in range(no_of_threads):
        worker = Thread(target=task, args=(barrier, i))
        worker.start()
    
    print('Main thread waiting on all results...')
    barrier.wait()
    print('All threads have their result')