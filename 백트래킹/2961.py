import sys
input = sys.stdin.readline



flavor = []
N = int(input())
result = 1e9
for i in range(N):
    x,y = map(int, input().split())
    flavor.append([x,y])

for bit in range(1, 1<<N):
    acidity, acerbity = 1, 0
    for i in reversed(range(N)):
        if bit&(1<<i):
            acidity*=flavor[i][0]
            acerbity+=flavor[i][1]
    result = min(result, abs(acidity-acerbity))

print(result)