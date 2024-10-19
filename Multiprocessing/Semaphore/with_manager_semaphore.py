from time import sleep
from random import random
from multiprocessing import Process, Manager

# target task function
def task(semaphore, number):
    with semaphore:
        # begin processing
        value = random()
        sleep(2)
        print(f'Thread {number} got {value}')
    

if __name__ == "__main__":
    # create a shared semaphore object with manager
    with Manager() as manager:
        
        semaphore = manager.Semaphore(4)
        
        # create a suite of processes
        processes = []
        for i in range(5):
            process = Process(target=task, args=(semaphore, i))
            processes.append(process)
            process.start()
            
        # block for a moment
        print('Main thread blocking...')
        
        for p in processes:
            p.join()
            
        print("End main")