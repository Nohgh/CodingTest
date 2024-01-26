import sys
input=sys.stdin.readline
arr1=[]
arr2=[]
sum=0
rst=[]
for _ in range(int(input())):
    sum=0
    a,b,c,d,e,f,g=map(int,input().split())
    if a>b:
        sum+=a
    else:
        sum+=b
    arr2.append(c)
    arr2.append(d)
    arr2.append(e)
    arr2.append(f)
    arr2.append(g)
    arr2.sort(reverse=True)
    sum+=(arr2[0]+arr2[1])
    rst.append(sum)
    arr2.clear()
rst.sort(reverse=True)
print(rst[0])