import sys
from collections import deque
input=sys.stdin.readline
q=deque()
n=int(input())
for _ in range(n):
    s=input().strip()
    if s=='pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif s=='size':
        print(len(q))
    elif s=='empty':
        if q:
            print(0)
        else:
            print(1)
    elif s=='front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif s=='back':
        if q:
            print(q[len(q)-1])
        else:
            print(-1)        
    else:
        a,num=s.split()
        q.append(num)