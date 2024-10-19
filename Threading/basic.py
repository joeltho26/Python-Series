
# https://stackoverflow.com/questions/25391025/what-exactly-is-python-multiprocessing-modules-join-method-doing

from threading import Thread
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.2)

thread = []
num_of_threads = 10

for i in range(num_of_threads):
    p = Thread(target=square_numbers)
    thread.append(p)

if __name__ == '__main__':
    for t in thread:
        t.start()
        
    for t in thread:
        t.join() # => wait for all the threads to complete and then only print the main thread 'end main'
        
    print('end main')