
from multiprocessing import Process, cpu_count, current_process, parent_process
from time import sleep
from random import random

processes = []
num_of_process = cpu_count()

def square_numbers():
    value = random() * 10
    sleep(2)
    print(f"Square of {value} is {value ** 2}")
    print(f"current process: {current_process()}")
    print(f"parent process: {parent_process()}")
    
if __name__ == "__main__":

    print(f"current process: {current_process()}")
    
    for i in range(num_of_process):
        p = Process(target=square_numbers)
        processes.append(p)

    if __name__ == '__main__':
        for p in processes:
            p.start()
            
        for p in processes:
            p.join() # => wait for all the process to complete and then only print the main thread 'end main'
            
        print('end main')