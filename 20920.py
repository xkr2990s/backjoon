import sys

num = sys.stdin.readline().split()
dic = {}

for _ in range(int(num[0])):
  str = sys.stdin.readline().strip()
  if len(str) >= int(num[1]):
    if str in dic:
      dic[str]+= 1
    else:
      dic[str] = 1

dic = sorted(dic.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in dic:
  print(i[0])