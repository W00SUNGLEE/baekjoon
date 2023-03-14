import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

lis_list = [0]

for i in range(len(num_list)):
    if lis_list[-1] < num_list[i]:
        lis_list.append(num_list[i])

    else:
        left = 0
        right = len(lis_list)

        while left < right:
            mid = (left + right) // 2

            if lis_list[mid] < num_list[i]:
                left = mid + 1

            else:
                right = mid

        lis_list[right] = num_list[i]

print(len(lis_list) - 1)
