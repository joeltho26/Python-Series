from time import sleep
from random import random
from threading import Thread
from threading import Condition
 
# target function
def task(condition, work_list):
    # acquire the condition
    with condition:
        # block for a moment
        value = random()
        sleep(value)
        # add work to the list
        work_list.append(value)
        print(f'Thread added {value}')
        # notify the waiting thread
        condition.notify()
        
if __name__ == "__main__":
    # create a condition
    condition = Condition()
    # define work list
    work_list = list()
    # start a bunch of threads that will add work to the list
    
    for i in range(5):
        worker = Thread(target=task, args=(condition, work_list))
        worker.start()
        
    # wait for all threads to add their work to the list
    with condition:
        # wait to be notified
        condition.wait_for(lambda : len(work_list)==5)
        print(f'Done, got: {work_list}')