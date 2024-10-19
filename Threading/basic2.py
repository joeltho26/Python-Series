from threading import Thread
import time

def task(number, value):
    final_value = value * 2
    print(f"Thread {number} got value {final_value}")

if __name__ == "__main__":
    items = [1,2,3,4,5,6,7,8,9,10]
    
    count = 0
    for i in range(0,len(items),3):
        print(count)
        if len(items) - count > 2:
            thread1 = Thread(target=task, args=(i,items[i],))
            thread2 = Thread(target=task, args=(i+1,items[i+1],))
            thread3 = Thread(target=task, args=(i+2,items[i+2],))
            
            thread1.start()
            thread2.start()
            thread3.start()
            
            count += 3
        else:
            thread = Thread(target=task, args=(i,items[i],))
            thread.start()
            count += 1
        
        time.sleep(3)
                
