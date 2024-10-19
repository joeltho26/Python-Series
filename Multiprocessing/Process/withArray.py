from multiprocessing import Process, Array, Lock
from time import sleep

def square_numbers(lock, values):
    with lock:
        for i in range(len(values)):
            values[i] *= values[i]
            sleep(1)
    
if __name__ == "__main__":
    lock = Lock()
    values = Array('d',[1.0,2.0,3.0,4.0])
    print(f"Beginning array: {values[:]}")
    
    process1 = Process(target=square_numbers, args=(lock,values,))
    process2 = Process(target=square_numbers, args=(lock,values,))
        
    process1.start()
    process2.start()
        
    process1.join()
    process2.join()
        
    print(f"End array: {values[:]}")
        
    print("End main")