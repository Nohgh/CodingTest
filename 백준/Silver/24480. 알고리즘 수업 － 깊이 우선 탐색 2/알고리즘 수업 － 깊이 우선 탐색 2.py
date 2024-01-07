import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

# n: 정점의 수 , m: 간선의 수 , r:시작 정점
n,m,r=map(int,input().split())

graph=[[]*1 for _ in range(n+1)]#인접리스트 표현
for _ in range(m): #인접리스트 초기화
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):#인접리스트 오름차순
    graph[i].sort()
    graph[i].reverse()
visited=[False] * (n+1) #방문여부
order_n=[0]*(n+1)#방문 순서 저장
cnt=1

def dfs(v):
    global cnt
    #현재 노드를 방문 처리
    visited[v]=True
    order_n[v]=cnt
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            cnt+=1
            dfs(i)
dfs(r)
for x in range(1,n+1):
    print(order_n[x])
