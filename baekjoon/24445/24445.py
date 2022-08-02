import sys
import heapq
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
queue = deque(list())

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(graph[a], -b)
    heapq.heappush(graph[b], -a)

def bfs(R):
    count = [0]
    queue.append(R)

    while queue:
        i = queue.popleft()

        if visited[i] == 0:
            count[0] += 1
            visited[i] += count[0]
            while graph[i]:
                tmp = -(heapq.heappop(graph[i]))
                queue.append(tmp)

bfs(R)

for i in range(1, N + 1):
    print(visited[i])