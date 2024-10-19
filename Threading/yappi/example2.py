from yappi import start, stop, get_thread_stats, get_func_stats
import time
from threading import Thread

_NTHREAD = 3


def _work(n):
    time.sleep(n * 0.1)

start()

threads = []
# generate _NTHREAD threads
for i in range(_NTHREAD):
    t = Thread(target=_work, args=(i + 1, ))
    t.start()
    threads.append(t)
    
# wait all threads to finish
for t in threads:
    t.join()

stop()

# retrieve thread stats by their thread id (given by yappi)
threads = get_thread_stats()
for thread in threads:
    print(
        "Function stats for (%s) (%d)" % (thread.name, thread.id)
    )  # it is the Thread.__class__.__name__
    get_func_stats(ctx_id=thread.id).print_all()