import sys
import heapq
input = sys.stdin.readline

def get_smallest_node():
    min_val = float('INF')
    index = 0
    for i in range(1, node+1):
        if distance[i]<min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now  = heapq.heappop(q)
        if distance[now]< dist:
            continue
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))

node, edge = map(int, input().split())
snode = int(input())
graph = [[]for _ in range(node+1)]
for _ in range(edge):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))

distance = [float('INF')]*(node+1)
visited = [0]*(node+1)

dijkstra(snode)
for i in range(1,node+1):
    print(distance[i] if not distance[i]==float('INF') else 'INF')