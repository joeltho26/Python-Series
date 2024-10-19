
from threading import Thread
import time

database_value = 0

def update_value():
    global database_value
    local_copy = database_value
    local_copy += 1
    time.sleep(1)
    database_value = local_copy

if __name__ == "__main__":
    print(f"Start Value: {database_value}")
    
    for _ in range(2):
        thread = Thread(target=update_value)
        thread.start()
    
    thread.join() # race condition, thread trying to execute the same function simultaneously.
        
    print(f"Final Value: {database_value}") # => Race condition when both the thread accessing the same method at the same time
    
    print('end main')