import sys
import copy
from collections import deque
from itertools import combinations

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()
empty = list()
virus = list()

area = n * m
safeArea = 0
count = 3

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

    for j in range(m):
        if matrix[i][j] == 0:
            empty.append((i, j))
        elif matrix[i][j] == 1:
            count += 1
        else: # matrix[i][j] == 2:
            virus.append((i, j))

area -= count
combination = combinations(empty, 3)

for (x1, y1), (x2, y2), (x3, y3) in combination:
    tmpSafeArea = area
    tmpMatrix = copy.deepcopy(matrix)

    tmpMatrix[x1][y1] = 1
    tmpMatrix[x2][y2] = 1
    tmpMatrix[x3][y3] = 1

    deq = deque(virus)

    while deq:
        a, b = deq.popleft()
        if tmpMatrix[a][b] == -1 or tmpMatrix[a][b] == 1:
            continue

        else: # tmpMatrix[a][b] == 0 or tmpMatrix[a][b] == 2:
            tmpMatrix[a][b] = -1
            tmpSafeArea -= 1

            for moveX, moveY in move:
                if 0 <= a + moveX < n and 0 <= b + moveY < m and tmpMatrix[a + moveX][b + moveY] == 0:
                    deq.append((a + moveX, b + moveY))

    if tmpSafeArea > safeArea:
        safeArea = tmpSafeArea

print(safeArea)