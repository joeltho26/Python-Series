from threading import Condition, Thread

# Shared resource
shared_resource = []

# Consumer thread
def consumer(condition):
    with condition:
        while not shared_resource:
            print("Consumer is waiting...")
            condition.wait()
        item = shared_resource.pop(0)
        print("Consumer consumed item:", item)

# Producer thread
def producer(condition):
    with condition:
        item = "New item"
        shared_resource.append(item)
        print("Producer produced item:", item)
        condition.notify()


if __name__ == "__main__":
    # Condition variable
    condition = Condition()
    
    # Create and start the threads
    consumer_thread = Thread(target=consumer, args=(condition,))
    producer_thread = Thread(target=producer, args=(condition,))
    consumer_thread.start()
    producer_thread.start()