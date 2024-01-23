import sys
input=sys.stdin.readline
arr=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    arr.append((a,b))
arr.sort()
for x in arr:
    print(*x)
               