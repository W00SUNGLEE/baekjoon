import sys
from collections import defaultdict

t = int(sys.stdin.readline())

dic = defaultdict(int)

for _ in range(t):
    dic.clear()
    answer = 1

    n = int(sys.stdin.readline())

    for _ in range(n):
        name, dress = map(str, sys.stdin.readline().split())
        dic[dress] += 1

    keys = dic.values()

    for key in keys:
        answer *= key+1

    answer -= 1

    print(answer)