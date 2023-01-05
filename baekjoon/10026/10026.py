import sys
import copy

sys.setrecursionlimit(10**6)

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n = int(sys.stdin.readline())

matrix1 = list()

for _ in range(n):
    matrix1.append(list(sys.stdin.readline().strip()))

matrix2 = copy.deepcopy(matrix1)

def dfs1(x, y, color):
    for xi, yi in move:
        new_x = x + xi
        new_y = y + yi

        if 0 <= new_x < n and 0 <= new_y < n:
            if matrix1[new_x][new_y] == color:
                matrix1[new_x][new_y] = 'X'
                dfs1(new_x, new_y, color)

def dfs2(x, y, color):
    for xi, yi in move:
        new_x = x + xi
        new_y = y + yi

        if 0 <= new_x < n and 0 <= new_y < n:
            if color == 'R' or color == 'G':
                if matrix2[new_x][new_y] == 'R' or matrix2[new_x][new_y] == 'G':
                    matrix2[new_x][new_y] = 'X'
                    dfs2(new_x, new_y, color)

            else:
                if matrix2[new_x][new_y] == 'B':
                    matrix2[new_x][new_y] = 'X'
                    dfs2(new_x, new_y, color)

answer = [0, 0]

for i in range(n):
    for j in range(n):
        if matrix1[i][j] != 'X':
            answer[0] += 1
            color = matrix1[i][j]
            matrix1[i][j] = 'X'
            dfs1(i, j, color)

        if matrix2[i][j] != 'X':
            answer[1] += 1
            color = matrix2[i][j]
            matrix2[i][j] = 'X'
            dfs2(i, j, color)

print(answer[0], answer[1])