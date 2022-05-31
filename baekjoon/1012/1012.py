import sys

sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def func(x, y, n, m):
    arr[x][y] = 0

    for xi, yi in move:
        if 0 <= x + xi < n and 0 <= y + yi < m and arr[x + xi][y + yi] == 1:
            func(x + xi, y + yi, n, m)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    arr = [[0 for _ in range(M)] for _ in range(N)]

    answer = 0

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        arr[x][y] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                func(i, j, N, M)
                answer += 1

    print(answer)