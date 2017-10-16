# python "/Users/gimseonghun/Desktop/study-python/KSH/5/queue.py"
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue) # deque(['Eric', 'John', 'Michael'])

queue.append("Terry") 
print(queue) # deque(['Eric', 'John', 'Michael', 'Terry'])

print(queue.popleft()) # Erid
print(queue) # deque(['John', 'Michael', 'Terry'])
