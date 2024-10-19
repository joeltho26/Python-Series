
# https://stackoverflow.com/questions/25391025/what-exactly-is-python-multiprocessing-modules-join-method-doing

from multiprocessing import Process, cpu_count
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.2)

processes = []
num_of_process = cpu_count()

for i in range(num_of_process):
    p = Process(target=square_numbers)
    processes.append(p)

if __name__ == '__main__':
    for p in processes:
        p.start()
        
    for p in processes:
        p.join() # => wait for all the process to complete and then only print the main thread 'end main'
        
    print('end main')