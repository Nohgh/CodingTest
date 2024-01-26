import sys
input=sys.stdin.readline
for _ in range(int(input())):
    a=list(map(int,input().split()))
    a.sort()
    if a[3]-a[1]>3:
        print("KIN")
    else:
        print(a[1]+a[2]+a[3])
    a.clear()