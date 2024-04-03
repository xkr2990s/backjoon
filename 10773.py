import sys

time = int(sys.stdin.readline())
stack = []
result = 0

for _ in range(time):
  num = int(sys.stdin.readline())
  if num:  #자연수
    stack.append(num)
  else:
    if stack:
      stack.pop()
      

for i in stack:
  result += i

print(result)