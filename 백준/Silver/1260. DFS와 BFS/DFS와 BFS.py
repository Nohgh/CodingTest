import sys
input=sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**6)
n,m,v=map(int,input().split())

dfs_visited=[False]*(n+1)
bfs_visited=[False]*(n+1)

graph=[[] for _ in range(n+1)]
q=deque()

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for x in range(n+1):
    graph[x].sort()



def dfs(v):
    dfs_visited[v]=True
    print(v,end=' ')
    for x in graph[v]:
        if not dfs_visited[x]:
            dfs(x)

def bfs(v):
    bfs_visited[v]=True
    q.append(v)
    while(q):
        x=q.popleft()
        print(x,end=' ')
        for i in graph[x]:
            if not bfs_visited[i]:
                q.append(i)
                bfs_visited[i]=True

dfs(v)
print()
bfs(v)