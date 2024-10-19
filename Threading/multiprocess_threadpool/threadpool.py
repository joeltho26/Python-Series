from multiprocessing.pool import ThreadPool

#https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread
def foo(bar, baz):
    print("hello {0}".format(bar))
    return 'foo' + baz

pool = ThreadPool(processes=1)
async_result = pool.apply_async(foo, ('world', 'foo')) # tuple of args for foo
return_val = async_result.get()
print(return_val) 