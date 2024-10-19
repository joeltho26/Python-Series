from multiprocessing import Process, Manager, Queue, Condition
from time import sleep


def putItem(condition, q): 
	# Put a string into the queue 
	with condition:
		q.put('hello')
		sleep(5)
		condition.notify()


def getItem(condition, q): 
	with condition:
		condition.wait()
		print(q.get()) 
		

# The following code will only run if the script is run directly 
if __name__ == '__main__': 
	
	condition = Condition()
	q = Queue()

	# Create two instances of the Process class, one for each function 
	p1 = Process(target=getItem, args=(condition, q,)) 
	p2 = Process(target=putItem, args=(condition, q,)) 

	# Start both processes 
	p1.start() 
	p2.start()
	
	# wait for both processes 
	p1.join() 
	p2.join() 

	print("process completed!")
