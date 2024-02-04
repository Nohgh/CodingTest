import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
sum=0
sum_arr=[]
arr.sort()
# print(arr)
for x in arr:
    sum=sum+x
    sum_arr.append(sum)
rst=0
for x in sum_arr:
    rst+=x
print(rst)
