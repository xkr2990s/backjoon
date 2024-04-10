import sys

num = int(sys.stdin.readline())
gom = 0
list=set()

for _ in range(num):
  str = sys.stdin.readline().strip()
  if str=='ENTER':
    list.clear()
  else:
    if str not in list:
      gom+=1
      list.add(str)

print(gom)