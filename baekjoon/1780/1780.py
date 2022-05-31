import sys

arr = []
count = [0, 0, 0]

n = int(sys.stdin.readline())

for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

def func(x, y, N):
    if N == 1:
        #count[arr[x][y]+1] += 1
        if arr[x][y] == -1:
            count[0] += 1
        elif arr[x][y] == 0:
            count[1] += 1
        elif arr[x][y] == 1:
            count[2] += 1

        return None

    else:
        for i in range(N):
            for j in range(N):
                if arr[x+i][y+j] != arr[x][y]:
                    for a in range(x, x + N, N // 3):
                        for b in range(y, y + N, N // 3):
                            func(a, b, N // 3)

                    return None

        #count[arr[x][y]+1] += 1
        if arr[x][y] == -1:
            count[0] += 1
        elif arr[x][y] == 0:
            count[1] += 1
        elif arr[x][y] == 1:
            count[2] += 1

        return None

func(0, 0, n)

print(count[0])
print(count[1])
print(count[2])