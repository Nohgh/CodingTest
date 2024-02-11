from collections import deque
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    s=list(input().strip()) #수행할 함수
    n=int(input()) #배열에 들어있는 수의 개수
    a=input().strip() #배열 [ , , ]형태로 입력 받음 
    q=deque()
    isreverse=False
    iserror=False
    if n>0:
        arr=a[1:-1].split(',')
        for x in range(len(arr)):
            q.append(int(arr[x]))
    for x in s:
        if x == 'R':
            if isreverse:
                isreverse=False
            else:
                isreverse=True
        else:
            if q:
                if isreverse:
                    q.pop()
                else:
                    q.popleft()
            else:
                iserror=True
                print('error')
                break
    if not iserror:
        if isreverse:
            q.reverse()
        print("["+",".join(map(str,q))+"]")
    