import sys
input=sys.stdin.readline

n=int(input())
d=[-1]*10001
d[1]=1 #1: sk
d[2]=0 #0: cy
d[3]=1
for i in range(4,n+1):
    if d[i-1]==0 or d[i-3]==0:
        d[i]=1
    else:
        d[i]=0
if d[n]==1:
    print("SK")
else:
    print("CY")
