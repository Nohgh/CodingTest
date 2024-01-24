import sys
input=sys.stdin.readline
a=[]
for _ in range(int(input())):
    s=input().strip()
    l=len(s)
    if(a.count((l,s))==0):
        a.append((l,s))
a.sort()
for x in a:
    print(x[1])