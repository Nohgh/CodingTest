import sys
input=sys.stdin.readline
x=int(input())
n=64
cnt=0
while(1):
    if(n>x):
        n=n/2
    elif(n<x):
        x-=n
        n=n/2
        cnt+=1
    elif(x==n):
        cnt+=1
        break
print(cnt)