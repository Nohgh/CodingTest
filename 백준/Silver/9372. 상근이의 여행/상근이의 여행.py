import sys
from collections import deque
input=sys.stdin.readline

t=int(input()) #테스트 케이스
rst=[]
cnt=0
def bfs(v):
    global cnt

    q=deque([v])
    visited[v]=True
    while(q):
        z=q.popleft()
        cnt+=1
        for x in graph[z]:
            if not visited[x]:
                q.append(x)
                visited[x]=True

for _ in range(t): #테이스 케이스만큼 반복
    n,m=map(int,input().split()) #n:국가(정점의 수) m:비행기 종류(간선의 수)
    visited=[False]*(n+1)
    graph=[[] for _ in range(n+1)]
    for _ in range(m):#각 국가를 거치는 비행기 입력(m만큼, 간선입력 )
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    bfs(1)
    rst.append(cnt-1)
    cnt=0

for x in rst:
    print(x)