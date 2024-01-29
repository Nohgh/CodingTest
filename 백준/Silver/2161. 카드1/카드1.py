import sys
from collections import deque
q=deque()
input=sys.stdin.readline
n=int(input())
for x in range(1,n+1):
    q.append(x)
q2=deque()
while(len(q)!=1):
    q2.append(q.popleft())
    q.append(q.popleft())
q2.append(q[0])
print(*q2)