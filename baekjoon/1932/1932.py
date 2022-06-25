import sys

dp = list()

n = int(sys.stdin.readline())

for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().split())))

    if i > 0:
        for j in range(i+1):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else: # 0 < j < i:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))