import sys

stack = []
time = int(sys.stdin.readline())

for _ in range(time):
  order = sys.stdin.readline().split()
  if order[0]=='1':  #스택삽입
    stack.append(order[1])
  elif order[0]=='2':  #스택 삭제
    if stack: print(stack.pop())
    else: print(-1)
  elif order[0]=='3':  #스택 크기
    print(len(stack))
  elif order[0]=='4':  #스택 공백 유무
    if(stack): print(0)
    else: print(1)
  elif order[0]=='5':  #스택 탑 출력
    if(stack): print(stack[-1])
    else: print(-1)