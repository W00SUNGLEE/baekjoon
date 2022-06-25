n = int(input())

dp = [[0,1,1,1,1,1,1,1,1,1]]

for i in range(1,n):
    tmp = [0,0,0,0,0,0,0,0,0,0]
    for j in range(10):
        if j == 0:
            tmp[j+1] += dp[i-1][j]
        elif 0 < j < 9:
            tmp[j - 1] += dp[i - 1][j]
            tmp[j + 1] += dp[i - 1][j]
        else: # j == 9
            tmp[j - 1] += dp[i - 1][j]

    dp.append(tmp)

print(sum(dp[n-1])%1000000000)