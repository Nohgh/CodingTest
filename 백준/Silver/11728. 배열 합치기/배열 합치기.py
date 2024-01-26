import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr1=[]
arr2=[]
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=[]
arr3=arr1+arr2
arr3.sort()
print(*arr3)