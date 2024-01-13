import sys
input=sys.stdin.readline
n=int(input()) #수열 A의 크기 (1,000,000)
a=list(map(int,input().split())) # 수열 A의 원소(각 1,000,000)

# rst=[] # 순회하며 A(i)보다 큰 원소 삽입 할 리스트
sysout=[-1]*n # nge 숫자들 저장
stack=[]
stack.append(0)
for x in range(1,n):
    while stack and a[stack[-1]] < a[x]:
        sysout[stack.pop()]=a[x]
    stack.append(x)
print(*sysout)
'''데이터 100만, 1초 o(n)으로 풀어야함 '''
