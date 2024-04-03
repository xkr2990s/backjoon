import sys
from collections import deque

queue = deque([])
num = sys.stdin.readline().split()
for i in range(int(num[0])):
  queue.append(i+1)

print('<', end='')
while(True):
  if len(queue)==1:
    print(queue.pop(), end='')
    break
  else:
    queue.rotate(-1*int(num[1])+1)
    print(queue.popleft(), end='')
    print(', ', end='')
print('>')