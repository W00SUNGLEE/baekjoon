dp = [0 for _ in range(11)]
dp[0] = 1

for i in range(10):
    if i + 1 < 11:
        dp[i+1] += dp[i]

    if i + 2 < 11:
        dp[i+2] += dp[i]

    if i + 3 < 11:
        dp[i+3] += dp[i]

T = int(input())

for _ in range(T):
    n = int(input())
    print(dp[n])