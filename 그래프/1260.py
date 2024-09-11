import sys
from collections import deque
sys.setrecursionlimit(15000)

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                


node,edge,root = map(int, input().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(node+1):
    graph[i].sort()


visited = [0]*(node+1)
dfs(graph, root, visited)
print()
visited = [0]*(node+1)
bfs(graph, root, visited)