import sys
sys.setrecursionlimit(150000)

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(graph, i, visited)

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N+1):
    graph[i].sort()

cnt = 1
visited = [0]*(N+1)

dfs(graph, R, visited)

for i in range(1, N+1):
    print(visited[i])