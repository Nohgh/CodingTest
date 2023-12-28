arr=[]
maxLength=0
n=5
printString=''
for x in range(n):
  i=input()
  arr.append(i)
  if(len(i)>maxLength):
    maxLength=len(i)
# print(arr[0][0],arr[1][0],arr[2][0])

for w in range(maxLength):#10글자 짜리가 최대
  for x in range(n):#4번 입력 받음 
    #00 10 20  / 01 11 21 /  02 12 22 /.../09 19 29
    #여기서
    try:
      printString+=arr[x][w]
    except:
      printString+=""
      
    
print(printString)