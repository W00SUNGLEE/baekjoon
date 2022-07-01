import sys
from itertools import accumulate

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, 0)
accumulateArr = list(accumulate(arr))

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(accumulateArr[j]-accumulateArr[i-1])
