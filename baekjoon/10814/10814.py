import sys

n = int(input())
arr = []

for i in range(n):
    year, name = sys.stdin.readline().split()
    year = int(year)
    arr.append([year, i, name])

arr.sort(key=lambda x:[x[0], x[1]])

for i in range(n):
    print(arr[i][0], arr[i][2])