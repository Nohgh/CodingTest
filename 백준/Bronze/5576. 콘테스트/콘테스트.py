import sys
input=sys.stdin.readline
arr1=[]
arr2=[]
rst=[]
for _ in range(10):
    arr1.append(int(input()))
for _ in range(10):
    arr2.append(int(input()))
arr1.sort(reverse=True)
arr2.sort(reverse=True)
rst.append(arr1[0]+arr1[1]+arr1[2])
rst.append(arr2[0]+arr2[1]+arr2[2])

print(*rst)