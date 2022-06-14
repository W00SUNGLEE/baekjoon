import sys

n, m = map(int, sys.stdin.readline().split())
dic = dict()

for i in range(1,n+1):
    tmp = sys.stdin.readline().strip()
    dic[tmp] = i
    dic[str(i)] = tmp

for _ in range(m):
    print(dic[sys.stdin.readline().strip()])