N = int(input())
a = list(map(int, input().split()))
result = []
for i in range(N-2):
    for j in range(i+1, N-1):
        if a[i] in a[j:]:
            add = 0
            for m in range(i,j+1):
                add += a[m]
            result.append(add)

result.sort(reverse=True)

print(result[0])

for i in range (1, N-1):
    if result[0]!=result[i]:
        print(i)
        break