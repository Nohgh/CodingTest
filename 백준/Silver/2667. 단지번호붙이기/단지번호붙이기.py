#n,m 크기의 얼음 틀이 있다
#구멍이 뚤려있는 부분은 0 칸ㅁ낙이가 존재하는 부분은 1로 표시된다. 
#구멍이 뚫려있는 부분끼리 상,하 ,좌,우 로 붙어있는 경우 서로 연결되어 있다.
# 얼음틀의 모양이 주
# 어졌을때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시 오
#입력: 첫 번째 줄에 얼음 틀의 세로 길이n과 가로길이m이 주어진다.
#두번째 줄부터  n+1ㅂ전쨰 줄까지 얼음 틀의 형ㅌ ㅐ가 주어진다.
#이때 구멍이 뚤려있는  부분은 0 그렇지 않은 부분은 1이다
#출력: 한번에 만들 수 있는 아이스크림의 개수를 출력한다.
import sys
input=sys.stdin.readline
n=int(input()) #행과 열을 입력받음 
graph=[]
for i in range(n):
    graph.append(list(map(int,input().strip())))#그래플에 한줄씩 입력 받음
arr=[]
z=0
def dfs(x,y):
    global z
    if x<=-1 or x>=n or y<=-1 or y>=n: #방문할 dfs요소가 틀을 벗어나거나 -1을 넘길때 
        return False #거짓을 넘겨줌 
    if graph[x][y]== 1: #0이 아이스크림 넣을 수 있는 공간 0끼리 이어야함 
        graph[x][y]=0 #1로 바꿈
        z+=1
        dfs(x-1,y) #여기서부터 양방향으로 체크함 
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False #0이 아닌경우에는 true를 위에서 반환하지 않고 여기서 false를 반환한다.

result=0
for i in range(n):
    for j in range(n):
        z=0
        if dfs(i,j)==True: #n,m배열을 순회하며 각 요소에 대해 dfs를 실행한다. 실행하여 dfs가 true인 경우 즉 
            #1로 연결되어 있는 경우에만  result를 올린다.
            arr.append(z)
            result+=1
arr.sort()
print(result)
for x in arr:
    print(x)