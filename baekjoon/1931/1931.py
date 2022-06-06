import sys

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort()

answer = 1
endTime = arr[0][1]

for i in range(1,n):
    if endTime <= arr[i][0]:
        endTime = arr[i][1]
        answer += 1

    else:
        if endTime > arr[i][1]:
            endTime = arr[i][1]

print(answer)