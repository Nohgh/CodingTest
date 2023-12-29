import sys

input = sys.stdin.readline
n = int(input())
s = []
for _ in range(n):
  str = input()
  for x in str:
    if (x == ')'):
      if(len(s)>0):
        if (s[len(s) - 1] == '('):
          s.pop()
      else:
          s.append(')')

    elif (x == '('):
      s.append('(')

  if (len(s) > 0):
    print("NO")
  else:
    print("YES")
  s.clear()
