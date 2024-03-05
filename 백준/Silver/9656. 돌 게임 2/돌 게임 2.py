import sys
input=sys.stdin.readline
n=int(input())
ds=[-1]*1001
ds[1]=0 #창영이 win
ds[2]=1 #상근이 win
ds[3]=0
for i in range(4,n+1):
    if ds[i-1]==0 or ds[i-3]==0:
        ds[i]=1
    else:
        ds[i]=0

if ds[n]==0:
    print("CY")
else:
    print("SK")