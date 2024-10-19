from threading import Condition, Thread
import time


def task(condition):
    condition.acquire()
    print('addition of 1 to 10 ')
    add= 0
    for i in range (1 , 11):
        add = add+i
    print(add)
    condition.release()
print('the condition object is releases now')

if __name__ == "__main__":
    condition = Condition()

    t1 = Thread(target = task, args=(condition,))
    t1.start()
