
from threading import Thread, current_thread, Lock
from queue import Queue
import time

def worker(q, lock):
    while True:
        item = q.get() # -> thread-safe
        with lock:
            print(f" in {current_thread().name} got {item}")
        q.task_done()

if __name__ == "__main__":    
    q = Queue()
    lock = Lock()
    #q.put(1)
    #q.put(2)
    #q.put(3)
    #PUT ---> 3  2  1  -----> OUT
    
    #first = q.get() => FIFO => Value: 1
    
    # return an item if one is immediately available, else raise the Empty exception ('timeout' is ignored in that case).
    #fourth = q.get(block=False, timeout=2) 
    
    #q.task_done() => used once we complete processing each element in the queue
    
    #print(q.empty()) => return true if the queue is empty
    
    #q.join() # => to wait for all the element in the queue to complete and then process the main thread
    
    num_of_threads = 10
    for i in range(num_of_threads):
        thread = Thread(target=worker, args=(q, lock,))
        thread.daemon = True #=> thread dies after the main thread dies even if we have while loop as True.
        thread.start()
    
    for i in range(21):
        q.put(i) # -> thread-safe
        
    q.join()
    
    print('end main')