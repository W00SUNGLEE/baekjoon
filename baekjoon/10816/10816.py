import sys
from collections import defaultdict

dic = defaultdict(int)
n = int(input())
tmp = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    dic[tmp[i]] += 1

m = int(input())
tmp = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    print(dic[tmp[i]], end=" ")