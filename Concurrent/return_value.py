import concurrent.futures

#https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
def foo(bar):
    print('hello {}'.format(bar))
    return 'foo'

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(foo, 'world!')
    return_value = future.result()
    print(return_value)