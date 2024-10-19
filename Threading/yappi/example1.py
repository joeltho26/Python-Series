# used for checking thread stats and info
from yappi import set_clock_type, start, get_func_stats, get_thread_stats

def a():
    for _ in range(10000000):  # do something CPU heavy
        pass

set_clock_type("cpu") # Use set_clock_type("wall") for wall time
start()
a()

get_func_stats().print_all()
get_thread_stats().print_all()
