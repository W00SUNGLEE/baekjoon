import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
count = [0 for _ in range(m)]

arr.insert(0, 0)
count[0] += 1
for i in range(1, n+1):
    arr[i] = (arr[i] + arr[i-1]) % m
    count[arr[i]] += 1
answer = 0

for i in range(m):
    answer += (count[i] * (count[i]-1)) // 2

print(answer)