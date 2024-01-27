import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr2=[]
for x in arr:
    if arr2.count(x)>0:
        continue
    else:
        arr2.append(x)
arr2.sort()
print(*arr2)