import sys
input=sys.stdin.readline
arr=[]
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(*arr)