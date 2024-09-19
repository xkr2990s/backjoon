import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(graph,v,state):
    visited[v] = state
    for i in graph[v]:
        if visited[i]==state:
            return False
        if visited[i]==0:
            if not dfs(graph,i,-state):
                return False
    return True

t = int(input())
for _ in range(t):
    node,edge = map(int, input().split())
    graph = [[] for _ in range(node+1)]
    visited = [0]*(node+1)

    for _ in range(edge):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    result = True
    for i in range(1,node+1):
        if not visited[i]:
            if not dfs(graph,i,1):
                result = False
                break

    print('YES' if result else "NO")