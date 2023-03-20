import sys
import bisect

n = int(sys.stdin.readline())

a_dict = dict.fromkeys(map(int, sys.stdin.readline().split()), 0)

b_list = list(map(int, sys.stdin.readline().split()))

for a, index in enumerate(b_list):
    a_dict[index] = a

new_list = list()

for value in a_dict.values():
    s = bisect.bisect_left(new_list, value)

    if s != len(new_list):
        new_list[s] = value

    else:
        new_list.append(value)

print(len(new_list))
