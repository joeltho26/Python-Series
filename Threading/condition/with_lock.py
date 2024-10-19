from threading import Condition, Thread, Lock
import time

database_value = 0


def task(condition, number):
    global database_value
    with condition:
        local_copy = database_value
        local_copy += 1
        database_value = local_copy
        print(f"Thread {number} got value {database_value}")
        time.sleep(1)

if __name__ == "__main__":
    lock = Lock()
    condition = Condition(lock)

    for i in range(10):
        thread = Thread(target=task, args=(condition,i))
        thread.start()
