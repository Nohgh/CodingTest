import sys
input=sys.stdin.readline
arr=[]
n=int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()
for x in arr:
    print(x)