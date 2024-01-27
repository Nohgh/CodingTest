import sys
input=sys.stdin.readline
n=int(input())
arr=list(set(list(map(int,input().split()))))
arr.sort()
print(*arr)