def is_promising(x):
    for i in range(x):
            if board[i]==board[x] or abs(x-i)==abs(board[x]-board[i]):
                return False
    return True

def dfs(row):
    global cnt
    if row==n:
        cnt+=1
        return
    else:
        for i in range(n):
            board[row] = i
            if is_promising(row):
                 dfs(row+1)

n = int(input())
board = [0]*n
cnt = 0
dfs(0)

print(cnt)