import sys
input=sys.stdin.readline
arr=[]
for x in range(1,9):
    arr.append((int(input()),x))
arr.sort(reverse=True)
cnt=1
sum=0
arr2=[]
for x in arr:
    if cnt<6:
        sum+=x[0]
        arr2.append(x[1])
    cnt+=1
print(sum)
arr2.sort()
print(*arr2)