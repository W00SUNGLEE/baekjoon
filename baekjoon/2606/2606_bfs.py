import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

deq = deque()

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1

def bfs(v):
  visited[v] = 1
  deq.append(v)

  while deq:
    v = deq.popleft()

    for i in range(n+1):
      if graph[v][i] == 1 and visited[i] == 0:
        deq.append(i)
        visited[i] = 1

bfs(1)

cnt = 0
for i in range(n+1):
  if visited[i] == 1:
    cnt += 1
    
print(cnt-1)