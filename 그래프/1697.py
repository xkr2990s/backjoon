import sys
from collections import deque
sys.setrecursionlimit(10000)

input = sys.stdin.readline
max = 100000

def bfs(n):
    if start==end:
        return 0
    queue = deque([(n,0)])
    visited = [0]*(max+1)
    visited[n] = 1
    while queue:
        x, level = queue.popleft()
        for nx in (x-1, x+1, x*2):
            if 0<=nx<=max and not visited[nx]:
                visited[nx] = 1
                if nx==end:
                    return level+1
                queue.append((nx, level+1))
    return -1

start, end = map(int, input().split())
print(bfs(start))