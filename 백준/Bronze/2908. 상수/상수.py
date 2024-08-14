a,b=input().split()
a=list(a)
b=list(b)
a.reverse()
b.reverse()
newA=''
newB=''
for x in a:
    newA+=x
for x in b:
    newB+=x
newA=int(newA)
newB=int(newB)
if(newA>newB):
    print(newA)
else:
    print(newB)
