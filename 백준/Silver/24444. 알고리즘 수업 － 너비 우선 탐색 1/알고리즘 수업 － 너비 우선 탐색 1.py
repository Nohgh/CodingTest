import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정
from collections import deque
input=sys.stdin.readline
n,m,r=map(int,input().split()) # 정점 간선 시작정점
graph=[[]for _ in range(n+1)] #인접리스트 
visited=[False]*(n+1)
order_n=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for x in range(n+1):
    graph[x].sort()

cnt=0
def bfs(r):
    global cnt
    queue=deque([r])
    visited[r]=True
    cnt+=1
    order_n[r]=cnt
    while queue:
        v=queue.popleft()
        # print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                cnt+=1
                order_n[i]=cnt
bfs(r)
for x in range(1,n+1):
    print(order_n[x])