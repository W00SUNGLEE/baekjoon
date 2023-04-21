import sys

n = int(sys.stdin.readline())

max_list = [0, 0, 0]
min_list = [0, 0, 0]

for _ in range(n):
    input = list(map(int, sys.stdin.readline().split()))

    max_tmp = list()
    min_tmp = list()

    max_tmp.append(max(max_list[0], max_list[1])+input[0])
    max_tmp.append(max(max_list[0], max_list[1], max_list[2])+input[1])
    max_tmp.append(max(max_list[1], max_list[2])+input[2])

    min_tmp.append(min(min_list[0], min_list[1])+input[0])
    min_tmp.append(min(min_list[0], min_list[1], min_list[2])+input[1])
    min_tmp.append(min(min_list[1], min_list[2])+input[2])

    max_list = max_tmp
    min_list = min_tmp

print(max(max_list), min(min_list))
