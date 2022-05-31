import sys

T = int(sys.stdin.readline())

dp = [1, 1, 1, 2, 2]

for _ in range(T):
    n = int(sys.stdin.readline())-1

    if n < len(dp):
        print(dp[n])
        continue

    else:
        for i in range(len(dp), n+1):
            dp.append(dp[i-1]+dp[i-5])

        print(dp[n])
