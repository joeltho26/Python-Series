from time import sleep
from random import random
from multiprocessing import Process, Manager, Lock
from threading import BrokenBarrierError

def report():
    print("The threads have completed execution!")

# target task function
def task(barrier, number, lock):
    # begin processing
    with lock:
        value = random()
        sleep(value)
        print(f'Process {number} got {value}')
    try:
        barrier.wait()
    except BrokenBarrierError:
        print(f"Processes {number} didnt completed on time...")
    

if __name__ == "__main__":
    # create a shared event object with manager
    with Manager() as manager:
        barrier = manager.Barrier(5 + 1, timeout=10, action=report)
        lock = Lock()
        
        # create a suite of processes
        processes = []
        for i in range(5):
            process = Process(target=task, args=(barrier, i, lock))
            processes.append(process)
            process.start()
            
        # block for a moment
        print('Main thread blocking...')
        sleep(2)
        
        try:
            barrier.wait()
        except BrokenBarrierError:
            print("Barrier broken, process incomplete...")
            exit(0)
        
        for p in processes:
            p.join()
            
        print("End main")