import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

queue = deque(list())
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

visited[0][0][0] = 1

queue.append((0, 0, 0))

answer = -1

while queue:
    x, y, broken = queue.popleft()

    if x == n-1 and y == m-1:
        answer = visited[x][y][broken]
        break

    for xi, yi in move:
        new_x = x + xi
        new_y = y + yi

        if 0 <= new_x < n and 0 <= new_y < m:
            if broken == 0:
                if matrix[new_x][new_y] == '0' and visited[new_x][new_y][0] == 0:
                    visited[new_x][new_y][0] = visited[x][y][broken] + 1
                    queue.append([new_x, new_y, 0])

                elif matrix[new_x][new_y] == '1':
                    visited[new_x][new_y][1] = visited[x][y][broken] + 1
                    queue.append([new_x, new_y, 1])

            elif broken == 1:
                if matrix[new_x][new_y] == '0' and visited[new_x][new_y][1] == 0:
                    visited[new_x][new_y][1] = visited[x][y][broken] + 1
                    queue.append([new_x, new_y, 1])

print(answer)
