import sys
input = sys.stdin.readline
a=int(input())
b=int(input())
c=int(input())
rst=str(a*b*c)
for x in range(10):
    x=str(x)
    print(rst.count(x))
  