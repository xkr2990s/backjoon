import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,l):
    queue = deque([(x,y,l)])
    visisted[x][y] = 1
    while queue:
        x,y,l = queue.popleft()
        
        if x==ex and y==ey:
            return l
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visisted[nx][ny]:
                visisted[nx][ny] = 1
                queue.append((nx,ny,l+1))
    return -1

dx = [-2,-1,1,2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

t = int(input())
for _ in range(t):
    n = int(input())
    sx,sy = map(int, input().split())
    ex,ey = map(int, input().split())
    visisted = [[0 for _ in range(n)] for _ in range(n)]

    print(bfs(sx,sy,0))
