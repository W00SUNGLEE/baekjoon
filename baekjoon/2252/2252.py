import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

indegree = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

answer = []
queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    index = queue.popleft()
    answer.append(index)

    for new_index in graph[index]:
        indegree[new_index] -= 1

        if indegree[new_index] == 0:
            queue.append(new_index)

for index in answer:
    print(index, end=' ')
