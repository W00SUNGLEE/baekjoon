t = int(input())

dp = list()
tmpList = list()

for i in range(t):

    n, m = map(int, input().split())

    if m < len(dp):
        print(dp[m][n])

    else:
        for i in range(len(dp), m + 1):
            tmpList.clear()

            for j in range(0, i + 1):
                if j == 0 or j == i:
                    tmpList.append(1)

                else:
                    tmp = dp[i - 1][j - 1] + dp[i - 1][j]
                    tmpList.append(tmp)

            dp.append(tmpList.copy())

        print(dp[m][n])