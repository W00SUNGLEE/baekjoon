import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

dp = [arr[0]]
answer = arr[0]

for i in range(1, n):
    if dp[i-1] > 0:
        dp.append(dp[i-1]+arr[i])
    else:
        dp.append(arr[i])

    if dp[i] > answer:
        answer = dp[i]

print(answer)