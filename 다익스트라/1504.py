import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance =[float('INF')]*(node+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(queue, (dist+i[1], i[0]))
    return distance

node, edge = map(int, input().split())
graph = [[]for _ in range(node+1)]

for _ in range(edge):
    n1, n2, dist = map(int, input().split())
    graph[n1].append((n2,dist))
    graph[n2].append((n1,dist))

x,y = map(int, input().split())

dist1 = dijkstra(1)[x]+dijkstra(x)[y]+dijkstra(y)[node]
dist2 = dijkstra(1)[y]+dijkstra(y)[x]+dijkstra(x)[node]

result = min(dist1,dist2)

print(result if result!=float('INF') else -1)
