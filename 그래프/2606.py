import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(graph, i, visited)


computers = int(input())
edges = int(input())
network = [[] for _ in range(computers+1)]

for _ in range(edges):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)

cnt = 0
visited = [0]*(computers+1)

dfs(network, 1, visited)

print(cnt)