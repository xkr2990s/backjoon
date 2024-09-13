import sys
from collections import deque
sys.setrecursionlimit
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque([(x,y,1)])
    graph[x][y] = 0

    while queue:
        a,b,level = queue.popleft()
        
        if a == n-1 and b == m-1:
            return level
        
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]:
                queue.append((nx,ny,level+1))
                graph[nx][ny] = 0
    return -1
                

graph = []
n, m = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().strip())))

print(bfs(0,0))