import sys
from collections import deque

input=sys.stdin.readline
n=int(input())

ball=deque() #풍선 
in_ball=deque()
rst=[] #터진 풍선 순서

for x in range(1,1+n):
    ball.append(x)

in_ball=list(map(int,input().split())) #풍선 안 숫자

for _ in range(n):
    # 4 3 2 1
    #이면 x는 4번째인 -3
    if(len(ball)==1):
        rst.append(ball.pop())
        break
    x=in_ball[ball[0]-1] #해당 풍선안의 숫자로 매칭
    
    if x>0:
        # if x:
            # rst.append(ball.popleft())
            # ball.appendleft(ball.pop())
        if x>1:
            rst.append(ball.popleft())
            for _ in range(x-1):
                if len(ball)==0:break                
                ball.append(ball.popleft())
        elif x==1:
            rst.append(ball.popleft())
        
    else:#음수
        # print("음수, pop 하기 전",end=' ')
        rst.append(ball.popleft())
        x=-1*x
        for _ in range(x):
            ball.appendleft(ball.pop())
        # print("음수, pop한 후 ",end=' ')    
        # print(ball)

print(*rst)
