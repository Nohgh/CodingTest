import sys
from collections import deque

input = sys.stdin.readline
q = deque()
rst=[]
n,k = map(int,input().split())


for x in range(1, n + 1):
  q.append(x)
while(q):
    for x in range(k-1):
        q.append(q.popleft())
        # print(q)
    rst.append(q.popleft())
print("<",end='')
for x in range(len(rst)-1):
   print("%d, " %rst[x],end='')
print("%d>" %rst[len(rst)-1])

