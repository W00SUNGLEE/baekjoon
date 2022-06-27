import sys

n = int(sys.stdin.readline())

arr = list()

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

dp = list()
dp.append(arr[0])
if n == 1:
    print(dp[0])
    exit()

dp.append(arr[0]+arr[1])
if n == 2:
    print(dp[1])
    exit()

dp.append(max(dp[1], arr[0]+arr[2], arr[1]+arr[2]))
if n == 3:
    print(dp[2])
    exit()

for i in range(3, n):
    dp.append(max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i]))

print(dp[n-1])