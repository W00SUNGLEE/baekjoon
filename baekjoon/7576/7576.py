import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

m, n = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

deq = deque([])

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            deq.append((i, j, 0))

while deq:
    x, y, day = deq.popleft()

    for xi, yi in move:
        if 0<=x+xi<n and 0<=y+yi<m and matrix[x+xi][y+yi] == 0:
            matrix[x + xi][y + yi] = 1
            deq.append((x + xi, y + yi, day+1))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(-1)
            exit(0)

print(day)