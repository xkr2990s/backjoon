import sys
from collections import deque

queue = deque([])
num = int(sys.stdin.readline())
for i in range(num):
  queue.append(i+1)

while(True):
  if len(queue)==1:
    print(queue[0])
    break
  else:
    queue.popleft()
    queue.append(queue.popleft())
