import logging
from threading import Barrier, BrokenBarrierError, Lock, Thread
from time import time, sleep
from random import random
import logging
from datetime import datetime
import traceback

## Logging config
date_value = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(f"./Threading/barrier/log_file{date_value}.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

####################################

value = 0

def report():
    logger.info("Threads completed execution!")
    
def task(barrier, number, lock):
    #value = random() * 10
    global value
    with lock:
        local_copy = value
        local_copy += 1
        sleep(value)
        value = local_copy
        logger.info("Thread %s finished execution with value %s.", str(number), str(value))
    try:
        barrier.wait()
    except BrokenBarrierError:
        logger.error("Barrier with threads are broken: %s", traceback.format_exc())
    
def main(barrier, no_of_threads, lock):
    start = time()
    for  i in range(no_of_threads):
        thread = Thread(target=task, args=(barrier, i, lock))
        thread.start()
    logging.info("Main thread wait for other threads to complete...")
    try:
        barrier.wait()
        end = time()
        logger.info("Time taken: %s", str({start-end}))
        logger.info("All threads have got their result.")
    except BrokenBarrierError:
        logger.error("Some of the threads did not finish on time! %s", traceback.format_exc())


if __name__ == "__main__":
    barrier = Barrier(10 + 1, timeout=50, action=report)
    lock = Lock()
    threads = 10
    main(barrier,threads,lock)
        