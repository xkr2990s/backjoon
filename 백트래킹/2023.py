import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

N = int(input())

def dfs(n):
    if len(str(n))==N:
        print(n)
    for i in range(1,10):
        if i%2==0:
            continue
        if isPrime(n*10+i):
            dfs(n*10+i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)