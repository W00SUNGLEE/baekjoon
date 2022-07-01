import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [1]

for i in range(1, n):
    tmp = 0
    for j in range(0, i):
        if arr[j] < arr[i] and dp[j] > tmp:
            tmp = dp[j]
    dp.append(tmp+1)

print(max(dp))
