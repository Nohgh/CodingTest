import sys
a=int(sys.stdin.readline())
arr=[]
for x in range(a):
  n=int(sys.stdin.readline())
  arr.append(n)
arr.sort()
for i in arr:
  print(i)