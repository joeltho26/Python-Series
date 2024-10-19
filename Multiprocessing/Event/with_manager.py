from time import sleep
from random import random
from multiprocessing import Process, Manager

# target task function
def task(event, number):
    # wait for the event to be set
    event.wait()
    # begin processing
    value = random()
    sleep(value)
    print(f'Thread {number} got {value}')
    

if __name__ == "__main__":
    # create a shared event object with manager
    
    with Manager() as manager:
        event = manager.Event()
        
        # create a suite of processes
        processes = []
        for i in range(5):
            process = Process(target=task, args=(event, i))
            processes.append(process)
            process.start()
            
        # block for a moment
        print('Main thread blocking...')
        sleep(2)
        # start processing in all process
        event.set()
        
        for p in processes:
            p.join()
            
        print("End main")