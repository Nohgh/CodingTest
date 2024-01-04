import sys
input=sys.stdin.readline
a,b=map(int,input().split())

cnt=0
rst=0
for x in range(1,a+1):
    if(a%x==0):
        cnt+=1
        if(cnt==b):
            rst=x
            break
print(rst)