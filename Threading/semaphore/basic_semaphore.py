from threading import Semaphore, Thread
from time import sleep

def process_item(item):
    semaphore.acquire()                     # acquire the semaphore
    try:
        sleep(3)                            # simulate some processing time
        print(f'Processing item {item}')    # process the item
    finally:                                # Make sure we always release the semaphore
        semaphore.release()                 # release the semaphore

if __name__ == "__main__":
    
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # semaphore to limit the number of threads that can access the list simultaneously to 4
    semaphore = Semaphore(value=4)
    
    # create a list of threads to process the items
    threads = [Thread(target=process_item, args=(item,)) for item in items]
    [thread.start() for thread in threads]      # start all threads
    [thread.join() for thread in threads]       # wait for all threads to finish