import sys
from collections import defaultdict
import copy

arr = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

accumulate = []

dic = defaultdict(int)
accumulate.append(copy.deepcopy(dic))

for i in range(len(arr)):
    dic[arr[i]] += 1
    accumulate.append(copy.deepcopy(dic))

for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    print(accumulate[r+1][a]-accumulate[l][a])

