from collections import deque

data = deque()
data.append("Gelo")
element = data.popleft()

print(element, data)