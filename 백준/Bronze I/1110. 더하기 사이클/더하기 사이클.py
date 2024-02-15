import sys
input=sys.stdin.readline
num=int(input())
originNum=num
newN=0
cnt=0

while 1:
        if num<10:
            a=0
        else:
            a=num//10 #앞자리
        b=num%10 #뒷자리
        c=a+b
        c=c%10
        newN=(b*10)+c #새로운 숫자
        # print(newN)
        num=newN
        cnt+=1
        if num == originNum: break
print(cnt)