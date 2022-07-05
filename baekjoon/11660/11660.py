import sys
from collections import deque
from itertools import accumulate

n, m = map(int, sys.stdin.readline().split())

arr = deque(list())
for _ in range(n):
    arr.append(deque(map(int, sys.stdin.readline().split())))

acumulateArr = deque(list())

acumulateArr.append(deque([0 for _ in range(len(arr[0])+1)]))
for i in range(1, len(arr)+1):
    acumulateArr.append(deque(accumulate(arr[i-1])))
    acumulateArr[i].appendleft(0)

    for j in range(len(arr[0])+1):
        acumulateArr[i][j] += acumulateArr[i-1][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    answer = acumulateArr[x2][y2] - acumulateArr[x1-1][y2] - acumulateArr[x2][y1-1] + acumulateArr[x1-1][y1-1]

    print(answer)