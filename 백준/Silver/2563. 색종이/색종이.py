import sys

n = int(sys.stdin.readline())
arr = [[0] * 100 for _ in range(100)]
rst = n * 100
# print(rst)
for _ in range(n):
  a, b = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  for i in range(a, a + 10):
    for j in range(b, b + 10):
      # print(i,j)
      arr[i][j] = 1

sum = 0
for x in range(0, 100):
  for y in range(0, 100):
    if (arr[x][y] == 1):
      sum += 1
print(sum)
