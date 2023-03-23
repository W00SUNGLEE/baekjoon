import sys
import bisect

n = int(sys.stdin.readline())

line_list = [0 for _ in range(n)]

tmp_list = list()

for _ in range(n):
    tmp_list.append(list(map(int, sys.stdin.readline().split())))

tmp_list.sort()

answer_list = [tmp_list[0][1]]
order_list = [1]

for i in range(1, len(tmp_list)):
    index = bisect.bisect_left(answer_list, tmp_list[i][1])

    if tmp_list[i][1] > answer_list[-1]:
        answer_list.append(tmp_list[i][1])

    else:
        answer_list[index] = tmp_list[i][1]

    order_list.append(index+1)


print(n - len(answer_list))

length = len(answer_list)
answer2_list = list()

for i in range(len(order_list)-1, -1, -1):
    if order_list[i] == length:
        length -= 1

    else:
        answer2_list.append(tmp_list[i][0])

for i in range(len(answer2_list)-1, -1, -1):
    print(answer2_list[i])
