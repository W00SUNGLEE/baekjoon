n = int(input())

dp = [0, 1, 2]

if n <= 2:
    print(dp[n])
    exit(0)

else:
    for i in range(3, n+1):
        dp.append(dp[i-1]+dp[i-2])

    print(dp[n]%10007)