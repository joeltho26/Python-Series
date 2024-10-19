
from threading import Thread, Lock
import time

database_value = 0

def update_value(lock):
    global database_value
    lock.acquire()
    local_copy = database_value
    local_copy += 1
    time.sleep(1)
    database_value = local_copy
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    
    print(f"Start Value: {database_value}")
    
    for _ in range(2):
        thread = Thread(target=update_value, args=(lock,))
        thread.start()
    
    thread.join()

    print(f"Final Value: {database_value}")
    
    print('end main')