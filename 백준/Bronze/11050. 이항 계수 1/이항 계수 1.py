import sys
input=sys.stdin.readline
n,k=map(int,input().split())
def fac(num):
    if num==0:
        return 1
    return num * fac(num-1)
print(fac(n)//(fac(k)*(fac(n-k))))