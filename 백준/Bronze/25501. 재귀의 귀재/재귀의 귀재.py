import sys
input=sys.stdin.readline
cnt=0
def recursion(s,l,r,cnt):
    cnt+=1 
    if l>=r: 
        return 1,cnt
    elif s[l] !=s[r]: return 0,cnt
    else:
        return recursion(s,l+1,r-1,cnt)
def isPalindrome(s,cnt):
    return recursion(s,0,len(s)-1,cnt)
n=int(input())
for _ in range(n):
    s=input().strip()
    a,b=isPalindrome(s,cnt)
    print(a,b)