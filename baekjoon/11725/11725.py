import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())

graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(n+1)]

answer = [0 for _ in range(n+1)]

queue = deque()

visited[0] = 1
visited[1] = 1
queue.append(1)

while queue:
    index = queue.popleft()

    for next_index in graph[index]:
        if visited[next_index] == 0:
            visited[next_index] = 1
            queue.append(next_index)
            answer[next_index] = index


for i in range(2, n+1):
    print(answer[i])
