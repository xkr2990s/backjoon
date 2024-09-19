import copy
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque([(0,0,1)])
    visited[0][0][1] = 1
    while queue:
        x,y,status = queue.popleft()
        if (x,y) == (n-1,m-1):
            return visited[x][y][status]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny][status] and not graph[nx][ny]:
                    visited[nx][ny][status] = visited[x][y][status]+1
                    queue.append((nx,ny,status))
                elif status and graph[nx][ny]:
                    visited[nx][ny][status-1] = visited[x][y][status]+1
                    queue.append((nx,ny,status-1))
    return -1
    

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
n,m = map(int, input().split())
visited = [[[0]*2 for _ in range(m)]for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().strip())))

print(bfs())