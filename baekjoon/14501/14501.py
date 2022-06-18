import sys

n = int(sys.stdin.readline().strip())
arr = list()

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [0 for _ in range(n+1)]
tmp = 0

for i in range(n):
    if tmp < dp[i]:
        tmp = dp[i]
    if dp[i] < tmp:
        dp[i] = tmp
    if i+arr[i][0] < n+1 and arr[i][1]+tmp > dp[i+arr[i][0]]:
        dp[i + arr[i][0]] = arr[i][1]+tmp

print(max(dp[n], tmp))