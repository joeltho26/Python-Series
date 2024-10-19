from time import sleep
from multiprocessing.pool import Pool
 
# result callback function
def handler():
    try:
        print(f'Callback got: {result}', flush=True)
    except TypeError:
        print("Handler doesn't take any arguments")
 
# custom function executed in another process
def task():
    # block for a moment
    sleep(1)
    return 'all done'
 
# protect the entry point
if __name__ == '__main__':
    # create and configure the process pool
    with Pool() as pool:
        try:
            # issue tasks to the process pool
            result = pool.apply_async(task, callback=handler)
            # get the result
            value = result.get()
            print(value)
        except TypeError:
            print("Handler doesn't take any arguments")
            