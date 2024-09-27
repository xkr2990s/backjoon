import sys
input = sys.stdin.readline

def dfs(i, result):
    global max_value, min_value, add, sub, mul, div
    if i==n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    else:
        if add>0:
            add-=1
            dfs(i+1,result+num[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,result-num[i])
            sub+=1
        if mul>0:
            mul-=1
            dfs(i+1,result*num[i])
            mul+=1
        if div>0:
            div-=1
            dfs(i+1,int(result/num[i]) if result>=0 else -(-result//num[i]))
            div+=1

        

max_value = -sys.maxsize
min_value = sys.maxsize

n = int(input())
num = list(map(int, input().split()))
add,sub,mul,div = map(int, input().split())

dfs(1, num[0])

print(max_value)
print(min_value)