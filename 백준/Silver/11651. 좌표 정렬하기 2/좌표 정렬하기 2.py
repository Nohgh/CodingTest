import sys
input=sys.stdin.readline
arr=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    arr.append((b,a))
arr.sort()
for x in arr:
    print(x[1],x[0])
               