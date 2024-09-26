import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def row(x,n):
    if x in board[n]:
        return False
    return True
def col(x,n):
    for i in range(9):
        if x==board[i][n]:
            return False
    return True
def square(x,a,b):
    for i in range(3):
        for j in range(3):
            if x==board[a//3*3+i][b//3*3+j]:
                return False
    return True

def sudoku(n):
    if n==len(blank):
        for i in board:
            print(*i)
        exit()
    x = blank[n][0] # 1
    y = blank[n][1] # 4
    for i in range(1,10): # 3
        if row(i,x) and col(i,y) and square(i,x,y):
            board[x][y] = i
            sudoku(n+1)
            board[x][y] = 0     # 백트래킹


board = [(list(map(int, input().split()))) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        if not board[i][j]:
            blank.append([i,j])

sudoku(0)