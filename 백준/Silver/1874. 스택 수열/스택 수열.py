import sys
input=sys.stdin.readline

n=int(input())
to_print=[]
st=[]
pl_mn=[]
for _ in range(n):
    to_print.append(int(input()))

a=1
t=0
canOut=True
for x in to_print:
    if(x>=a):
        while(x>=a):
            st.append(a)
            pl_mn.append('+')
            a+=1
        st.pop()
        pl_mn.append('-')
    else: 
        while(st):
            t=st.pop()
            pl_mn.append('-')
            if(t==x):
                break
        if len(st)==0 and t!=x:
            canOut=False
            print("NO")
            break
if(canOut==True):
    for x in pl_mn:
        print(x)