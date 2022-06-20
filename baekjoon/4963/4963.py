import sys

sys.setrecursionlimit(10000)

move = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

def dfs(x, y, w, h):
    matrix[x][y] = 0

    for xi, yi in move:
        if 0<=x+xi<h and 0<=y+yi<w and matrix[x+xi][y+yi] == 1:
            dfs(x + xi, y + yi, w, h)

while True:
    answer = 0
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        exit(0)

    else:
        matrix = list()

        for _ in range(h):
            matrix.append(list(map(int, sys.stdin.readline().split())))

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 1:
                    answer += 1
                    dfs(i, j, w, h)

        print(answer)