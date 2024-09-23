import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000

def bfs(v):
    visited = [-1]*(MAX+1)
    q = deque([v])
    visited[v] = 0
    while q:
        loc = q.popleft()
        if loc==end:
            return visited[loc]
        for nx in (loc*2,loc-1,loc+1):
            if 0<=nx<=MAX and visited[nx]==-1:
                if nx==loc*2:
                    visited[nx] = visited[loc]
                else:
                    visited[nx] = visited[loc]+1
                q.append(nx)
    return -1


start, end = map(int, input().split())

print(bfs(start))