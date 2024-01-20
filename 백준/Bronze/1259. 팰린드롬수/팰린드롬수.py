import sys
input=sys.stdin.readline
arr=[]
isSame='yes'
while(1):
    s=input().strip()
    if(s=='0'):
        break
    for x in reversed(s):
        arr.append(x)
        
    for x in range(len(s)):
        if arr[x]!=s[x]:
            isSame='no'
    print(isSame)
    isSame='yes'
    arr.clear()