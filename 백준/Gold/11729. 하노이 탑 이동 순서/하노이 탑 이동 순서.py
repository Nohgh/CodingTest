#하노이의 탑
import sys
input=sys.stdin.readline
n=int(input())
cnt=0
rst=[]
def hanoi(num,nw,nxt,spt): # 5 1 3 2
    global cnt
    if(num==1):
        s=str(nw)+" "+str(nxt)
        rst.append(s)
        cnt+=1
        return
    else:
        hanoi(num-1,nw,spt,nxt) #원판 4개를 1에서 2로 옮김 3은 보조
        s=str(nw)+" "+str(nxt)
        rst.append(s)
        cnt+=1
        hanoi(num-1,spt,nxt,nw)
hanoi(n,1,3,2)
print(cnt)
for x in rst:
    print(x)