import sys
input=sys.stdin.readline

n=int(input())
arr1=list(map(int,input().split()))
arr1.sort()
m=int(input())
arr2=list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start>end:
        return 0
    mid=(start+end)//2
    if array[mid]==target:
        return 1
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)
rst=[]
for x in arr2:
    rst.append(binary_search(arr1,x,0,n-1))
print(*rst)