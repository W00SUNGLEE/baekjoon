import sys

n = int(sys.stdin.readline())

train_list = list()

for _ in range(n):
    train_list.append(int(sys.stdin.readline()))

lis = [0 for _ in range(n)]
lds = [0 for _ in range(n)]

answer = 0

for i in range(n-1, -1, -1):
    lis[i] = 1
    lds[i] = 1

    for j in range(i+1, n):
        if train_list[j] > train_list[i]:
            lis[i] = max(lis[i], lis[j] + 1)

        elif train_list[j] < train_list[i]:
            lds[i] = max(lds[i], lds[j] + 1)

    answer = max(answer, lis[i] + lds[i] - 1)

print(answer)