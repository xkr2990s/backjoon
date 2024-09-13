import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=m:
        return False
    if graph[x][y]:
        graph[x][y] = 0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])


for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j]:
                cnt+=1
                dfs(i,j)

    print(cnt)