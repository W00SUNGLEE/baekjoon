import sys
from collections import Counter
from collections import defaultdict

arr = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

dic = defaultdict(int)
dic[-1] = defaultdict(int)

for _ in range(n):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)
    if dic[l-1] == 0:
        dic[l-1] = Counter(arr[:l])
    if dic[r] == 0:
        dic[r] = Counter(arr[:r+1])
    print(dic[r][a] - dic[l-1][a])