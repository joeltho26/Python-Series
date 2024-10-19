from multiprocessing import Process, set_start_method, get_start_method

# https://www.geeksforgeeks.org/understanding-fork-and-spawn-in-python-multiprocessing/?ref=ml_lbp

# initialize the value
num = 10
def childprocess():

	# refer to the global variable
	global num 
	print(f"In child process before update: {num}")

	#updating num value
	num+= 1
	print(f"In child process after update: {num}")


def mainprocess():

	# refer to the global variable
	global num 
	print(f"In parent process before update {num}")

	#updating num value
	num = 20

	# execution logic
	print(f"In parent process after update: {num}")
	process = Process(target = childprocess)
	process.start()
	process.join()
	print(f"At the end the vaule is: {num}")

if __name__ == '__main__':

	# setting start method as fork
	set_start_method('spawn')
	print(get_start_method())
	mainprocess()
