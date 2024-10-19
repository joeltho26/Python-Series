from threading import Condition, Thread
import time

def task(condition, number, value):
    with condition:
        final_value = value * 2
        print(f"Thread {number} got value {final_value}")
        time.sleep(3)

if __name__ == "__main__":
    condition = Condition()
    items = [1,2,3,4,5,6,7,8,9]
    for i in range(0,len(items),3):
        thread1 = Thread(target=task, args=(condition,i,items[i],))
        thread2 = Thread(target=task, args=(condition,i+1,items[i+1],))
        thread3 = Thread(target=task, args=(condition,i+2,items[i+2],))
        
        thread1.start()
        thread2.start()
        thread3.start()
                
