import sys

arr = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

arrLen = len(arr)

accumulate = [[0 for _ in range(26)] for _ in range(arrLen+1)]

for i in range(1, arrLen+1):
    for j in range(26):
        accumulate[i][j] = accumulate[i-1][j]
    accumulate[i][ord(arr[i-1])-97] += 1

for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    print(accumulate[r+1][ord(a)-97] - accumulate[l][ord(a)-97])