import sys
input=sys.stdin.readline
arr=[]
cnt=0
for _ in range(int(input())):
    cnt+=1
    s=input().strip()
    a,b=s.split()
    a=int(a)
    arr.append((a,cnt,b))
arr.sort()
for x in arr:
    print(x[0],x[2])
