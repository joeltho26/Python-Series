import time
from threading import Event, Thread

class product:

    def buyer(self):
        print('John consumer is wait for product') 
        print('...............')
        event_object.wait() 
        print('got product')	 

    def seller(self): 
        time.sleep(5)
        print('Tom producer producing items') 
        print('tom goes to retailer')
        event_object.wait()
        
    def retailer(self):
        time.sleep(10)
        print('retailer found that product and directly send to buyer')
        event_object.set()
		

# setting event object
if __name__=='__main__':
    # class object	 
    class_obj = product()
    
    event_object = Event()

    # creating threads
    T1 = Thread(target=class_obj.buyer)
    T2 = Thread(target=class_obj.seller)
    T3 = Thread(target=class_obj.retailer)

    # starting threads
    T1.start()
    T2.start()
    T3.start()
