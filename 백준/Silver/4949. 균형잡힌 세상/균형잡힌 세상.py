import sys

s = []
dot=0
input = sys.stdin.readline
#0[)](0)
#([)]())
#[)()]
while (1):
  str = input()
  if (str[0] == '.'):
    break
  # line = sys.stdin.readline().rstrip("\n")

  for x in str:

    if (x == '.'):
      if(x.count('.')==dot):
        continue
      else:
        dot+=1
    else:  
      if (x == '[' or x == ']' or x == '(' or x == ')'):
        if (x == '[' or x == '('):
          s.append(x)
  
        elif (x == ')'):
          if (len(s) <= 0):
            s.append(x)
          elif (s[len(s) - 1] == '('):
            s.pop()
          elif(s[len(s) - 1] != '('):
            s.append(x)
  
        elif (x == ']'):
          if (len(s) <= 0):
            s.append(x)
          elif (s[len(s) - 1] == '['):
            s.pop()
          elif(s[len(s) - 1] != '['):
            s.append(x)
  
  if (len(s) > 0):
    print("no")
  else:
    print("yes")
  s.clear()
