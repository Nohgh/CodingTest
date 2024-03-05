import sys
input=sys.stdin.readline
n=int(input())

# dp=[[-1,-1]]*46
dp=[[0,0] for _ in range(46)]


# 첫번째가  a개수 두번째가 b의 개수
dp[1]=[0,1]
dp[2]=[1,1]
dp[3]=[1,2]
for i in range(3,n+1):
    dp[i][0]=dp[i-1][1]
    dp[i][1]=dp[i-1][0]+dp[i-1][1]
print(*dp[n])

