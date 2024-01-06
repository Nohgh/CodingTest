import sys
arr=[]
while(1):
    a,b,c=map(int,sys.stdin.readline().split())
    arr.append(a)
    arr.append(b)
    arr.append(c)
    arr.sort()
    if a==b==c==0:
        break
    else:
        if arr[2]**2==arr[0]**2+arr[1]**2:
            print("right")
        else:
            print("wrong")
    arr.clear()
