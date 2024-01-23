import sys
input=sys.stdin.readline
a=[]
sum=0
for _ in range(5):
    n=int(input())
    a.append(n)
    sum+=n
a.sort()
print(sum//5)
print(a[2])
