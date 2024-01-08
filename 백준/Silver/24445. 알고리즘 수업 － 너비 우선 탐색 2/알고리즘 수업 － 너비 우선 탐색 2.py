import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정
from collections import deque
input=sys.stdin.readline



n,m,r=map(int,input().split()) # 정점 간선 시작정점
graph=[[]for _ in range(n+1)] #인접리스트 
visited=[False]*(n+1) # 방문 여부 체크
order_n=[0]*(n+1) # 방문순서 출력


for _ in range(m):
    a,b=map(int,input().split()) #두 정점으로 연결된 간선을 입력받고 그래프의 인접리스트에 추가
    graph[a].append(b)
    graph[b].append(a)

for x in range(n+1):
    graph[x].sort() #인접리스트 각 행에 대해 오름차순으로 정렬
    graph[x].reverse()
cnt=0 # 몇 번째에 방문했는지

def bfs(r):
    global cnt 
    queue=deque([r]) #들어온 정점을 큐에 push
    visited[r]=True #정점 방문 표시
    cnt+=1 
    order_n[r]=cnt 
    while queue:# 큐가 공백일때 까지 
        v=queue.popleft() #큐에서 가장 앞에 넣은거 pop한 원소 저장
        # print(v,end=' ')
        for i in graph[v]: #pop한 원소의 인접리스트에 대해 (인접 모든 원소)
            if not visited[i]: #방문하지 않았다면 
                queue.append(i) #큐에 삽입
                visited[i]=True #방문 표시
                cnt+=1
                order_n[i]=cnt
            
bfs(r)
for x in range(1,n+1):
    print(order_n[x])