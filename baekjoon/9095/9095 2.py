dp = [0, 1, 2, 4]

T = int(input())

for _ in range(T):
    n = int(input())

    if n < len(dp):
        print(dp[n])

    else:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])

        print(dp[n])