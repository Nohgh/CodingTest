import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
rst=[]
for i in range(n):
    rst.append(arr[i]+(i+1))
rst.sort(reverse=True)
print(rst[0]+1)