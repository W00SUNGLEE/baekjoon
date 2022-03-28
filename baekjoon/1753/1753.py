import sys
import heapq
INF = sys.maxsize
v, e = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())

graph = [[] for i in range(v+1)]
distances = [INF for _ in range(v+1)]

for i in range(e):
  v1, v2, w = map(int, sys.stdin.readline().split())
  graph[v1].append([v2, w])

def dijkstra(graph, start):
  distances[start] = 0
  heapque = []
  heapq.heappush(heapque, [distances[start], start])

  while heapque:
    v1_distance, v1 = heapq.heappop(heapque)

    if v1_distance > distances[v1]:
      continue
    
    for v2, v2_distance in graph[v1]:
      distance = v1_distance + v2_distance
      if distance < distances[v2]:
        distances[v2] = distance
        heapq.heappush(heapque, [distance, v2])

dijkstra(graph, start)

for i in range(1,v+1):
  if distances[i] != INF:
    print(distances[i])
  else:
    print("INF")