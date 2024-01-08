import sys
str=sys.stdin.readline().strip()
boom=sys.stdin.readline().strip()
boom_len=len(boom)
boom_list=[]
s=[]
for x in range(boom_len):
    boom_list.append(boom[x])
for x in range(len(str)):
    s.append(str[x])
    if(len(s)>=boom_len ):
        if(s[len(s)-boom_len:]==boom_list):
            for _ in range(boom_len):
                s.pop()
if(s):
    for x in s:
        print(x,end='')
else:
    print("FRULA")