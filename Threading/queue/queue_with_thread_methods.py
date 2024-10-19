
from threading import Thread, current_thread, RLock, get_ident, active_count
from threading import get_native_id, main_thread
from queue import Queue
import time

def worker(q, rlock):
    while True:
        item = q.get() # -> thread-safe
        with rlock:
            print(f" in {current_thread().name} got {item}, active thread counts: {active_count()}")
            print(f"get_native_id {get_native_id()}")
            print(f"thread identifier: {get_ident()}")
            
        q.task_done()
        if q.empty() is True:
            break

if __name__ == "__main__":    
    q = Queue()
    
    # https://stackoverflow.com/questions/22885775/what-is-the-difference-between-lock-and-rlock
    rlock = RLock()
    
    num_of_threads = 10
    for i in range(num_of_threads):
        thread = Thread(target=worker, args=(q, rlock,))
        thread.daemon = False
        thread.start()

    print(f"{main_thread.__class__.__name__}")
    
    for i in range(21):
        q.put(i) # -> thread-safe
        
    q.join()
    
    print('end main')