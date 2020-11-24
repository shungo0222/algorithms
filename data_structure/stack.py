# add, delete or get elements only at both ends -> deque O(1)
# frequently access to elements other than both ends -> list O(1)

# LIFO(Last In First Out)

from collections import deque

d = deque(['a', 'b', 'c'])
print(d)

d.append('d')
print(d)

d.popleft()
print(d)

d.appendleft('e')
print(d)

d.pop()
print(d)