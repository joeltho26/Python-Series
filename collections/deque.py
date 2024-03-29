from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
print(list(queue))
queue.appendleft(5)
print(list(queue))
queue.pop()
print(list(queue))
queue.append(30)
print(list(queue))
queue.popleft()
print(list(queue))
queue.remove(30)
print(list(queue))
queue.append(40)
queue.extend([50,60,70,10])
print(list(queue))
print(queue.count(10))
queue.extendleft((1,2,3))
print(list(queue))
queue.reverse()
print(list(queue))
queue_copy = queue.copy()
print(list(queue_copy))
queue_copy.clear()
print(queue_copy)
queue.insert(2,13)
print(list(queue))
print(queue.index(1))
queue.rotate(2)
print(list(queue))
del queue_copy
print(queue_copy)