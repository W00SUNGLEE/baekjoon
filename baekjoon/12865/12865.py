import sys

n, k = map(int, sys.stdin.readline().split())

weight_value_list = [[0, 0]]


for _ in range(n):
    weight_value_list.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < weight_value_list[i][0]:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight_value_list[i][0]] + weight_value_list[i][1])

print(dp[n][k])
