import sys
from collections import deque
input=sys.stdin.readline


n=int(input())
l=int(input())

visited=[False]*(n+1)
graph=[[]for _ in range(n+1)]

for _ in range(l):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(n+1):
    graph[x].sort()
q=deque()
cnt=0
def bfs(x):
    global cnt
    visited[x]=True
    q.append(x)
    while(q):
        v=q.popleft()
        cnt+=1
        visited[v]=True
        for z in graph[v]:
            if not visited[z]:
                q.append(z)
                visited[z]=True

bfs(1)

print(cnt-1)