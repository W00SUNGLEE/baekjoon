import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    matrix = [[0 for _ in range(100000)] for _ in range(2)]

    # for _ in range(2):
    #     matrix.append(list(map(int, sys.stdin.readline().split())))

    for i, var in enumerate(map(int, sys.stdin.readline().split())):
        matrix[0][i] = var
    for i, var in enumerate(map(int, sys.stdin.readline().split())):
        matrix[1][i] = var

    dp = [[0 for _ in range(100000)] for _ in range(2)]

    dp[0][0] = matrix[0][0]
    dp[1][0] = matrix[1][0]

    dp[0][1] = dp[1][0] + matrix[0][1]
    dp[1][1] = dp[0][0] + matrix[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i - 1] + matrix[0][i], dp[1][i - 2] + matrix[0][i])
        dp[1][i] = max(dp[0][i - 1] + matrix[1][i], dp[0][i - 2] + matrix[1][i])

    print(max(dp[0][n - 1], dp[1][n - 1]))
