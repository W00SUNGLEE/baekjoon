import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n)]

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(n):
    tmp = sys.stdin.readline()
    for j in range(m):
        arr[i].append(int(tmp[j]))

#bfs
deq = deque([(0, 0, 1)])
arr[0][0] = 0

while deq:
    x, y, count = deq.popleft()
    if x == n-1 and y == m-1:
        answer = count
        break

    for xi, yi in move:
        if 0 <= x+xi < n and 0 <= y+yi < m and arr[x+xi][y+yi] == 1:
            arr[x + xi][y + yi] = 0
            deq.append((x+xi, y+yi, count+1))

print(answer)
