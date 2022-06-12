from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
dic = defaultdict(int)

for i in range(n):
    dic[arr[i]] = 1

m = int(input())
arr = list(map(int, input().split()))

for i in range(m):
    print(dic[arr[i]], end=" ")