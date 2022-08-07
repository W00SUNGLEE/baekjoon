n = int(input())

arr = [0 for _ in range(n+1)]

for i in range(0, n+1, 5):
    arr[i] = 1

for i in range(0, n+1, 25):
    arr[i] = 2

for i in range(0, n+1, 125):
    arr[i] = 3

arr[0] = 0

print(sum(arr))