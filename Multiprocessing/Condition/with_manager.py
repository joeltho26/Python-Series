from multiprocessing import Process, Manager, Queue, Condition
from time import sleep


def putItem(condition, q):
    # Put a string into the queue
    with condition:
        q.put('hello')
        condition.notify()


def getItem(condition, q):
    with condition:
        condition.wait()
        print(q.get())

if __name__ == '__main__':
    with Manager() as manager:
        q = manager.Queue()
        condition = manager.Condition()

        p1 = Process(target=getItem, args=(condition, q,))
        p2 = Process(target=putItem, args=(condition, q,))

        p1.start()
        p2.start()

        p1.join()
        p2.join()