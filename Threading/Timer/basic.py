from time import sleep
from threading import Timer

# target task function
def task(message):
    # report the custom message
    print(message)

# create a thread timer object
timer = Timer(3, task, args=('Hello world',))

# start the timer object
timer.start()

# wait for the timer to finish
print('Waiting for the timer...')
sleep(7)

# cancel the thread
print('Canceling the timer...')
timer.cancel()