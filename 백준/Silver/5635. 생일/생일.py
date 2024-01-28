import sys
input=sys.stdin.readline
arr=[]
n=int(input())
for _ in range(n):
    name,day,month,year=input().strip().split()
    day=int(day)
    month=int(month)
    year=int(year)
    arr.append((year,month,day,name))
arr.sort()
print(arr[n-1][3])
print(arr[0][3])