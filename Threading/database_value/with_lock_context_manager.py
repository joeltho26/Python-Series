
from threading import Thread, Lock
import time

database_value = 0

def update_value(lock):
    global database_value
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(1)
        database_value = local_copy

if __name__ == "__main__":
    lock = Lock()
    
    print(f"Start Value: {database_value}")
    thread1 = Thread(target=update_value, args=(lock,))
    thread2 = Thread(target=update_value, args=(lock,))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(f"Final Value: {database_value}")
    
    print('end main')