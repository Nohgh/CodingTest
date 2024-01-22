from collections import deque
import sys
input=sys.stdin.readline

q=deque()
for _ in range(int(input())):
    s=input().strip()
    if s == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif s=='pop_back':
        if q:
            print(q.pop())
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
        a,b=s.split()
        b=int(b)
        if a=='push_front':
            q.appendleft(b)
        else:
            q.append(b)