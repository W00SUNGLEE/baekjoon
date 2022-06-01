import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())

visited = [0 for _ in range(N+1)]

dic = defaultdict(list)

answer = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)

def dfs(index):
    visited[index] = 1

    for i in range(len(dic[index])):
        if visited[dic[index][i]] == 0:
            dfs(dic[index][i])

for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        answer += 1

print(answer)