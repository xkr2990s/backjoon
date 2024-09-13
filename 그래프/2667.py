import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    graph.append(list(map(int, input().strip())))

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y]:
        global cnt
        cnt+=1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

cnt = 0
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])