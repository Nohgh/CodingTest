import sys
input = sys.stdin.readline
arr=list(map(int,input().split()))
asc_n=1
desg_n=8
for x in arr:
    if(x==asc_n):
        asc_n+=1
    if(x==desg_n):
        desg_n-=1
if(asc_n==9):
  print("ascending")
elif(desg_n==0):
    print("descending")
else:
    print("mixed")