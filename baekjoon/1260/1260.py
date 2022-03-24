import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

deq = deque()

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a][b] = 1
  graph[b][a] = 1

def dfs(v):
  visited[v] = 1

  print(v, end=' ')

  for i in range(1, n+1):
    if graph[v][i] == 1 and visited[i] == 0:
      dfs(i)

def bfs(v):
  visited[v] = 0
  deq.append(v)

  while deq:
    v = deq.popleft()
    
    print(v, end=' ')
    
    for i in range(1, n+1):
      if graph[v][i] == 1 and visited[i] == 1:
        deq.append(i)
        visited[i] = 0
        
dfs(v)
print()
bfs(v)