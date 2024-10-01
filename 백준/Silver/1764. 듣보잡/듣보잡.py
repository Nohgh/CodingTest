n,m=map(int,input().split())
a=set()
b=set()
arr=[]
for _ in range(n):
    a.add(input())
    
for _ in range(m):
    b.add(input())

for x in a:
    if x in b:
        arr.append(x)
        
arr.sort()

print(len(arr))
for x in arr:
    print(x)