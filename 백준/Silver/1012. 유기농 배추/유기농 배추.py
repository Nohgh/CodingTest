import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if arr[x][y]==1:
        arr[x][y]=0
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x-1,y)
        return True 
    return False


rst=[]
t=int(input())

for _ in range(t):
    m,n,k=map(int,input().split()) #가로:m 세로:n 배추개수:k 
    #n개의행, m개의 열
    arr=[[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split()) #배추의 위치 x(0~m-1) y(0~n-1)
        #k줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.
        #x는 가로 y는 새로  새로가 행 가로가 열 
        # 2 1 이 들어오면 arr[1][2]에 1이 들어와야 함 
        # 2 3 이 들어오면 2행 3열
        #x=m열 y=n행
        arr[y][x]=1
        # arr[x][y]=1

    result=0
    for i in range(n):
        for j in range(m):
            re=dfs(i,j)
            if re==True:
                #arr[i][j]   j가 열 
                result+=1
    rst.append(result)

for x in rst:
    print(x)
#8 4는 arr[4][8]