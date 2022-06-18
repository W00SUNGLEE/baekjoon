import sys

n = int(sys.stdin.readline().strip())

dp = [[0, 0, 0]]

for i in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    dp.append([min(dp[i][1]+r, dp[i][2]+r), min(dp[i][0]+g, dp[i][2]+g), min(dp[i][0]+b, dp[i][1]+b)])

print(min(dp[n]))