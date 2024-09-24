import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [1e9]*(node+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, current = heapq.heappop(q)
        if distance[current]<dist:
            continue
        for i in graph[current]:
            if dist+i[1]<distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
    return distance

T = int(input())
for _ in range(T):
    node,edge,candidate = map(int, input().split())
    s,g,h = map(int, input().split())
    graph = [[] for _ in range(node+1)]
    cands = []

    for _ in range(edge):
        u,v,w = map(int, input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))

    for i in range(candidate):
        cands.append(int(input()))

    start = dijkstra(s)
    g_dijk = dijkstra(g)
    h_dijk = dijkstra(h)

    result = []

    for cand in cands:
        if start[g]+g_dijk[h]+h_dijk[cand] == start[cand] or start[h]+h_dijk[g]+g_dijk[cand] == start[cand]:
            result.append(cand)

    result.sort()

    for i in result:
        print(i, end=' ')
    print()