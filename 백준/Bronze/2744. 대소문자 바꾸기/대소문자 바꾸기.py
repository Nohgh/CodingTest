import sys
input=sys.stdin.readline
s=input()
for x in s:
    if x.isupper()==True:
        print(x.lower(),end='')
    else:
        print(x.upper(),end='')