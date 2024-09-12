import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


N = int(input())
graph = []
num = []

for _ in range(N):
    graph.append(list(map(int, input().strip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    
def dfs(x,y):
    if x<0 or x>=N or y<0 or y>=N:
        return False
    if graph[x][y]:
        global cnt
        cnt +=1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

cnt = 0
result =0

for i in range(N):
    for j in range(N):
        if dfs(i,j):
            num.append(cnt)
            result +=1
            cnt = 0

num.sort()

print(result)
for i in range(result):
    print(num[i])