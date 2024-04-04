import sys
from collections import deque

deque = deque([])
time = int(sys.stdin.readline())

for _ in range(time):
    order = sys.stdin.readline().split()
    if order[0]=='1':
        deque.appendleft(order[1])
    elif order[0]=='2':
        deque.append(order[1])
    elif order[0]=='3':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif order[0]=='4':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif order[0]=='5':
        print(len(deque))
    elif order[0]=='6':
        if deque:
            print(0)
        else:
            print(1)
    elif order[0]=='7':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif order[0]=='8':
        if deque:
            print(deque[-1])
        else:
            print(-1)
