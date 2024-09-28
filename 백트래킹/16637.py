import sys
input = sys.stdin.readline


def calculate(a, oper, b):
    if oper=='+':
        return a+b
    elif oper=='-':
        return a-b
    elif oper=='*':
        return a*b


def dfs(index, result):
    global max_value
    
    if index >= n-1:
        max_value = max(max_value, result)
        return
    
    if index+2 < n:
        next_result = calculate(result, s[index+1], int(s[index+2]))
        dfs(index+2, next_result)
    
    if index+4 < n:
        next_result = calculate(result, s[index+1], calculate(int(s[index+2]), s[index+3], int(s[index+4])))
        dfs(index+4, next_result)


n = int(input())
s = list(input().strip())
max_value = -1e9

dfs(0, int(s[0]))

print(max_value)