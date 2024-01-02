import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n=int(input())

for _ in range(n):
  s=input().strip()
  if(len(s)>1):
      a,b=map(int,s.split())
      
  else:
      a=int(s)


  if(a==1):
      q.appendleft(b)

  elif(a==2):
      q.append(b)

  elif(a==3):
      if(q):
          print(q.popleft())
      else:
          print(-1)

  elif(a==4):   
      if(q):
          print(q.pop())
      else:
          print(-1)

  elif(a==5):
      print(len(q))

  elif(a==6):
      if(q):
          print(0)
      else:
          print(1)
      
  elif(a==7):
      if(q):
          print(q[0])
      else:
          print(-1)
  elif(a==8):
      if(q):
          print(q[len(q)-1])
      else:
          print(-1)