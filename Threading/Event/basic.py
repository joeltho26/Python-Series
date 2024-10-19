from time import sleep
from random import random
from threading import Thread, Event

# https://superfastpython.com/thread-event-object-in-python/
# https://www.geeksforgeeks.org/implement-inter-thread-communication-with-event-method-in-python/

# target task function
def task(event, number):
    # wait for the event to be set
    event.wait()
    # begin processing
    value = random()
    sleep(value)
    print(f'Thread {number} got {value}')
 
# create a shared event object
event = Event()
# create a suite of threads
for i in range(5):
    thread = Thread(target=task, args=(event, i))
    thread.start()
# block for a moment
print('Main thread blocking...')
sleep(2)
# start processing in all threads
event.set()