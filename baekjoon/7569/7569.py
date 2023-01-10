import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

move = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

matrix = list()

queue = deque()

for i in range(h):
    tmp_list = list()

    for j in range(n):
        tmp_list.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if tmp_list[j][k] == 1:
                queue.append((i, j, k, 0))

    matrix.append(tmp_list)

while queue:
    x, y, z, count = queue.popleft()

    for xi, yi, zi in move:
        new_x = x+xi
        new_y = y+yi
        new_z = z+zi
        if 0 <= new_x < h and 0 <= new_y < n and 0 <= new_z < m:
            if matrix[new_x][new_y][new_z] == 0:
                matrix[new_x][new_y][new_z] = 1
                queue.append((new_x, new_y, new_z, count+1))
                answer = count+1

check = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                check = False
                break

        if not check:
            break

    if not check :
        break

if check:
    print(count)
else:
    print(-1)
