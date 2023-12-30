import sys
from collections import deque

# n = int(input())
n = int(sys.stdin.readline())
# q = []
q = deque()

for _ in range(n):
  s = sys.stdin.readline().strip()
  if (s.count(' ') > 0):
    a, b = s.split()
    q.append(b)
  else:
    if s == "pop":
      if len(q) > 0:
        print(q.popleft())
      else:
        print(-1)

    elif s == 'size':
      print(len(q))

    elif s == 'empty':
      if (len(q) > 0):
        print(0)
      else:
        print(1)

    elif s == 'front':
      if len(q) > 0:
        print(q[0])
      else:
        print(-1)

    elif s == 'back':
      if len(q) > 0:
        print(q[len(q) - 1])
      else:
        print(-1)
