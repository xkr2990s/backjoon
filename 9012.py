import sys

time = int(sys.stdin.readline())
for _ in range(time):
  list = []
  state = 1
  str = input()
  for char in str:
    if char=='(':
      list.append(char)
    elif char==')':
      if list:
        list.pop()
      else:
        print("NO")
        state = 0
        break;
  if state:
    if list: print("NO")
    else: print("YES")