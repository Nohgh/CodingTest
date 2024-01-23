import sys
input=sys.stdin.readline
n=input().strip()
a=[]
for x in n:
    a.append(int(x))
a.sort(reverse=True)
for x in a:
    print(x,end='')