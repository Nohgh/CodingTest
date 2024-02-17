import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
max=0

a.sort(reverse=True)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        for h in range(j+1,len(a)):
            if max< a[i]+a[j]+a[h] and a[i]+a[j]+a[h]<=m :
                max=a[i]+a[j]+a[h]
print(max)