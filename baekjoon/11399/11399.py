import sys

n = int(input())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

answer = 0

for i in range(n):
    answer += arr[i]*(n-i)

print(answer)