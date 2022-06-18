import sys
from collections import defaultdict

dic = defaultdict(int)

n = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    dic[arr[i]] = 1

m = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    print(dic[arr[i]])