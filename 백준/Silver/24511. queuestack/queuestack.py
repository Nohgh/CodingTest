import sys
input = sys.stdin.readline
from collections import deque

n=int(input()) #줄 1
q_or_s=list(map(int,input().split())) #줄 2
qs=list(map(int,input().split())) #줄 3
m=int(input()) #줄 4
push_item=list(map(int,input().split())) #줄 5
q=deque()
cnt=0
rst=deque()
for x in reversed(range(n)):
    if q_or_s[x]==0:
        q.append(qs[x])
        cnt+=1
        if(cnt==m):
            break
for x in push_item:
    if(cnt==m):
        break
    q.append(x)
    cnt+=1
    
print(*q)
