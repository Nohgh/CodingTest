import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()
for x in range(1, n + 1):
  q.append(x)
while (len(q) != 1):
  q.popleft()
  a = q.popleft()
  q.append(a)
print(q[0])
