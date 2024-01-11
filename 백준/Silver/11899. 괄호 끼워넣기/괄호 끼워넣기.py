import sys
s=sys.stdin.readline().strip()
st=[]
for x in s: # ) )
    if(len(st)==0):
        st.append(x)# (
    else:
        if(x=='('):
            st.append(x) # ((
        else:
            if(st[len(st)-1]==')'):
                st.append(x)
            else:
                st.pop()
print(len(st))

