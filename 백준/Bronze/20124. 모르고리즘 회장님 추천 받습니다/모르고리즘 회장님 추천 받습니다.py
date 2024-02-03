import sys
input=sys.stdin.readline
a=[]
same=[]
max=0
for _ in range(int(input())):
    s,n=input().split()
    n=int(n)
    if n>=max:
        max=n
    a.append((n,s))
for x in a:
    if x[0]==max:
        same.append(x[1])
same.sort()
print(same[0])