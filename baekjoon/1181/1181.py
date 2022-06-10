import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().strip())

arr = list(set(arr))

arr.sort(key = lambda x: [len(x), x])

for word in arr:
    print(word)