import sys
import bisect

n = int(sys.stdin.readline())

line_list = [0 for _ in range(n)]

tmp_list = list()

for _ in range(n):
    tmp_list.append(list(map(int, sys.stdin.readline().split())))

tmp_list.sort()

answer_list = [tmp_list[0][1]]

for i in range(1, len(tmp_list)):
    if tmp_list[i][1] > answer_list[-1]:
        answer_list.append(tmp_list[i][1])

    else:
        index = bisect.bisect_left(answer_list, tmp_list[i][1])
        answer_list[index] = tmp_list[i][1]

print(n - len(answer_list))
