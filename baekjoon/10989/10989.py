import sys

n = int(sys.stdin.readline())
arr = [0]*10000

for i in range(n):
  arr[int(sys.stdin.readline())-1] += 1

for i in range(10001):
  for j in range(arr[i]):
    print(i+1)