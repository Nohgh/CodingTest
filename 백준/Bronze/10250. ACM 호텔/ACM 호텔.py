import sys
input = sys.stdin.readline
for x in range(int(input())):
    h,w,n=map(int,input().split())
    arr=[[0]*h for _ in range(w)]
    if(n%h==0):
        fst_s=str(h)
        scd_s=str((n//h))
    else:
        fst_s=str(n%h)
        scd_s=str((n//h)+1)
    if(len(scd_s)==1):
        print(fst_s+'0'+scd_s)
    else:
        print(fst_s+scd_s)

