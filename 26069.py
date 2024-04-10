import sys

meet = int(sys.stdin.readline())
chong = {'ChongChong'}

for _ in range(meet):
  str = sys.stdin.readline().split()
  if str[0] in chong or str[1] in chong:
    chong.add(str[0])
    chong.add(str[1])

print(len(chong))