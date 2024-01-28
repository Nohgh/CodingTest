import sys
input=sys.stdin.readline
arr=[]
for _ in range(int(input())):
    arr.append(int(input()))
arr=list(set(arr))
arr.sort(reverse=True)
for x in arr:
    print(x)