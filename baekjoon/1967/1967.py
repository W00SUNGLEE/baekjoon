import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

dic = defaultdict(lambda: defaultdict(int))

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())

    dic[a][b] = c
    dic[b][a] = c

def dfs(index):
    for i in dic[index].keys():

        if visited[i] == -1:
            visited[i] = visited[index] + dic[index][i]
            dfs(i)

node_length = len(dic.keys())

visited = [-1 for _ in range(n+1)]
visited[1] = 0
dfs(1)

start = visited.index(max(visited))

visited = [-1 for _ in range(n+1)]
visited[start] = 0
dfs(start)

print(max(visited))
