import sys

sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def func(x, y, n, m):
    for xi, yi in move:
        if 0 <= x+xi < n and 0 <= y+yi < m and (x+xi, y+yi) in arr:
            arr.remove((x+xi, y+yi))
            func(x+xi, y+yi, n, m)

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = []
    answer = 0

    for _ in range(K):
        y, x = map(int, sys.stdin.readline().split())
        arr.append((x, y))

    while arr:
        i, j = arr.pop()
        func(i, j, N, M)
        answer += 1

    print(answer)