import sys
from collections import deque
sys.setrecursionlimit(15000)

input = sys.stdin.readline

def bfs(graph, v, visited):
    global cnt
    queue = deque([v])
    visited[v] = cnt
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                queue.append(i)
                visited[i] = cnt


node, edge, root = map(int, input().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(node+1):
    graph[i].sort(reverse=True)

visited = [0]*(node+1)
cnt = 1

bfs(graph, root, visited)

for i in range(1, node+1):
    print(visited[i])