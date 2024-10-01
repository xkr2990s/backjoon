import sys
input = sys.stdin.readline


n = int(input())//2
s = input().strip()
max_value = -1e9

for bit in range(1<<n):
    if bit&(bit<<1):
        continue
    exp = [*s]
    for i in reversed(range(n)):
        if bit&(1<<i):
            exp.insert(i*2+3,')')
            exp.insert(i*2,'(')
    max_value = max(max_value, eval(''.join(exp)))

print(max_value)