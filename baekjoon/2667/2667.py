import sys

n = int(sys.stdin.readline())

arr = [[] for _ in range(n)]
count = []

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(n):
    tmp = sys.stdin.readline()
    for j in range(n):
        arr[i].append(int(tmp[j]))

def func(x, y):
    arr[x][y] = 0
    tmpCount[0] += 1

    for xi, yi in move:
        if 0 <= x+xi < n and 0 <= y+yi < n and arr[x+xi][y+yi] == 1:
            func(x+xi, y+yi)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            tmpCount = [0]
            func(i, j)
            count.append(tmpCount[0])

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])