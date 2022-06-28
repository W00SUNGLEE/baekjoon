import sys
from collections import deque

n, k = map(int, input().split())

deq = deque(list())
deq.append(n)
arr = [sys.maxsize for _ in range(100001)]
arr[n] = 0

while deq:
    x = deq.popleft()

    if x == k:
        print(arr[x])
        break

    if 0 <= 2*x <= 100000:
        if arr[x]+1 < arr[2*x]:
            arr[2*x] = arr[x]+1
            deq.append(2*x)
    if 0 <= x+1 <= 100000:
        if arr[x]+1 < arr[x+1]:
            arr[x+1] = arr[x] + 1
            deq.append(x+1)
    if 0 <= x-1 <= 100000:
        if arr[x]+1 < arr[x-1]:
            arr[x-1] = arr[x] + 1
            deq.append(x-1)