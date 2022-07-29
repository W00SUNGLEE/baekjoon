import sys
import heapq

sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(graph[a], b)
    heapq.heappush(graph[b], a)

count = [0]

def dfs(R):
    count[0] += 1
    visited[R] += count[0]

    while len(graph[R]) > 0:
        i = heapq.heappop(graph[R])
        if visited[i] == 0:
            dfs(i)

dfs(R)

for i in range(1, N+1):
    print(visited[i])