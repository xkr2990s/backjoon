import sys
from collections import deque
input = sys.stdin.readline


def bfs(n,cnt):
    queue = deque([(n,cnt)])
    
    while queue:
        x,cnt = queue.popleft()
        if x==100:
            return cnt
        board[x] = -1
        for i in range(1,7):
            nx = x+i
            if nx<=100:
                if board[nx]>0:
                    queue.append((board[nx],cnt+1))
                    board[nx] = -1
                elif board[nx]==0:
                    queue.append((nx,cnt+1))
    return 0

local = 0
board = [0]*(100+1)
ladder, snake = map(int, input().split())
for i in range(ladder):
    x,y = map(int, input().split())
    board[x] = y
for i in range(snake):
    x,y = map(int, input().split())
    board[x] = y

print(bfs(1,0))

