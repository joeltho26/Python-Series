
from threading import Thread, current_thread, Lock, get_ident, active_count
from threading import get_native_id, stack_size, enumerate, setprofile, getprofile, gettrace, settrace
from queue import Queue
import time


def trace():
    print(f"get_native_id {get_native_id()}")
    print(f"thread identifier: {get_ident()}")
    
def track_profile():
    print(f"active thread counts: {active_count()}")
    
def worker(q, lock):
    while True:
        item = q.get() # -> thread-safe
        #https://www.includehelp.com/python/threading-settrace-method-with-example.aspx
        settrace(trace())
        #https://www.includehelp.com/python/threading-setprofile-method-with-example.aspx
        setprofile(track_profile())
        with lock:
            print(f" in {current_thread().name} got {item}")
        q.task_done()

if __name__ == "__main__":    
    q = Queue()
    lock = Lock()
    
    num_of_threads = 10
    
    # https://superfastpython.com/thread-stack-size-in-python/
    print(stack_size()) # => if 0 returned then it means uses the default stack size    
    
    for i in range(num_of_threads):
        thread = Thread(target=worker, args=(q, lock,))
        thread.daemon = True
        thread.start()
        
    # return the list of all the Thread class objects which are currently alive. 
    # It also includes daemonic threads, the main thread, and dummy thread objects created by current_thread(). 
    # It does not count the threads that have terminated or which have not started yet.
    # https://www.includehelp.com/python/threading-enumerate-method-with-example.aspx
    print(enumerate()) 

    for i in range(21):
        q.put(i) # -> thread-safe
        
    q.join()
    
    print('end main')