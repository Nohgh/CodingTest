import sys
input=sys.stdin.readline
arr=set()
for _ in range(int(input())):
    name,log=input().strip().split()
    if log=="enter":
        arr.add(name)
    else:
        arr.discard(name)
# print(arr)
arr=list(arr)
arr.sort(reverse=True)
for x in arr:
    print(x)