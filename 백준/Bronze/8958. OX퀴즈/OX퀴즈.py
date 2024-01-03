import sys
input = sys.stdin.readline
sum=0
for _ in range(int(input())):
    str=input().strip()
    cntZero=0
    for x in str:
        if(x=='o'or x=='O'):
            cntZero+=1
        else:
            for z in range(1,cntZero+1):
                sum+=z
            cntZero=0
    for x in range(1,cntZero+1):
        sum+=x

    print(sum)
    sum=0
    cntZero=0