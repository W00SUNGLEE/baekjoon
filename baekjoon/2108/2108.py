import sys
import statistics
import collections

n = int(sys.stdin.readline())

arr = [0 for _ in range(n)]

for i in range(n):
    arr[i] = int(sys.stdin.readline())

arr.sort()

print(round(statistics.mean(arr)))
print(statistics.median(arr))
collectArr = collections.Counter(arr)
mode = max(collectArr.values())
modeArr = []
for key, value in collectArr.items():
    if value == mode:
        modeArr.append(key)

if len(modeArr) == 1:
    print(modeArr[0])
else:
    print(modeArr[1])

print(arr[n-1]-arr[0])