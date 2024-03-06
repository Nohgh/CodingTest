import sys
input=sys.stdin.readline
n=int(input())

dp=[0]*1001
dp[1]=1 #n=1, 세로는 2 고정, 가로의 길이가 1, 1*2타일 하나만 가능
dp[2]=2

for i in range(3,n+1):
    dp[i]=(dp[i-1]+(dp[i-2]))%10007
print(dp[n])
