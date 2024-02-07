import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(gragh,v,visited):
    visited[v]=True
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh,i,visited)
n,m=map(int,input().split())
visited=[False]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)



count=0
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        count+=1
print(count)