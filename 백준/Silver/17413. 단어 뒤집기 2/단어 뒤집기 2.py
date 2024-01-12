import sys
s=sys.stdin.readline().strip()
st1=[]
rst=[]
inParse=False
for x in s:
    if inParse==False and x=='<': #<를 만나고 <안이 아닐경우에
        while st1:
            rst.append(st1.pop())
        inParse=True #<안이라고 표시하고
        rst.append(x) #출력 배열에 <를 바로 넣는다.

    elif inParse==True and x=='>': #>라면
        rst.append(x) #>를 넣고 st1에 있는 값을 담음
        inParse=False

    elif inParse==True and x==' ':#괄호안에 공백이 있는 경우 
        rst.append(x)

    elif inParse==False and x==' ':#괄호 밖이고 공백을 만난 경우 
        while st1:
            rst.append(st1.pop()) #st1에 넣은 문자를 역으로 출력할 수 있게함
        rst.append(x)#공백을 추가해줌
    else:
        if inParse==True:
            rst.append(x)
        else:
            st1.append(x)
if len(st1)>0:
    while st1:
        rst.append(st1.pop())

for x in rst:
    print(x,end='')