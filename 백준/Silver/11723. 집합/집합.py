import sys
input=sys.stdin.readline
s=set()
for _ in range(int(input())):
    in_str=input().strip()
    if in_str.count(' ')>0:
        a,x=in_str.split()
        x=int(x)
    else:
        a=in_str
    if a=='add':
        s.add(x)
    elif a=='remove':
        s.discard(x)
    elif a=='check':
        if x in s:
            print(1)
        else:
            print(0)
    elif a=='toggle':
        if x in s:
            s.discard(x)
        else:
            s.add(x)
    elif a=='all':
        s.update([1,2,3,4,5,6,7,8,9,10
                  ,11,12,13,14,15,16,17,18,19,20])
    else:
        s.clear()