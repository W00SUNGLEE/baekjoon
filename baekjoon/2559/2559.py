import sys
from itertools import accumulate

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

arr.insert(0, 0)

arr = list(accumulate(arr))

answer = -sys.maxsize

for i in range(len(arr)-m):
    tmp = arr[i+m]-arr[i]

    if tmp > answer:
        answer = tmp

print(answer)