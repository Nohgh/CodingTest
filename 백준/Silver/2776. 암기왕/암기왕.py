import sys
input=sys.stdin.readline
            
def b_s(array,target,start,end):
    if start > end:
        return 0
    mid=(start+end)//2
    if target==array[mid]:
        return 1
    elif array[mid]>target:
        return b_s(array,target,start,mid-1)
    else:
        return b_s(array,target,mid+1,end)

for _ in range(int(input())):
    n=int(input())
    arr1=list(map(int,input().split()))

    m=int(input())
    arr2=list(map(int,input().split()))

    arr1.sort()
    for x in arr2:
        rst=b_s(arr1,x,0,n-1)
        print(rst)
