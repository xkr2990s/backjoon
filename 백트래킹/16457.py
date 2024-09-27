'''
    key = 3, quest = 4, skill = 2
    ktoq = 
        q1 = 1 3
        q2 = 1 2
        q3 = 2 3
        q4 = 3 6
    keys = 1,2,3,6

    keys에서 3개를 뽑아서 ktoq와 비교하면서 뽑은 퀘스트에 필요한 키가 뽑은 키에 있을 때 1을 추가한다. 
'''


import sys
input = sys.stdin.readline

def dfs(prev, n):
    global max_value
    # 키 선택 완료
    if n==key:
        result = sum(all(k in batch for k in q) for q in ktoq)
        max_value = max(max_value, result)
        return
    
    for i in range(prev+1,key*2+1):
        batch[n] = i
        dfs(i, n+1)



key, quest, skill = map(int, input().split())
ktoq = [list(map(int, input().split())) for _ in range(quest)]
keys = sorted(set(k for q in ktoq for k in q))
batch = [0 for _ in range(key)]
max_value = 0

dfs(0,0)

print(max_value)