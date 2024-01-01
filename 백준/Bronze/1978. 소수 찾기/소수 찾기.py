import sys
n=int(sys.stdin.readline())
a=[]
rst=0
a=list(map(int,sys.stdin.readline().split()))
for x in a:
    if(x==1):
        continue
    for y in range(2,x+1):
        if( x%y==0):
            if(x==y):
                rst+=1
            else:
                break
print(rst)