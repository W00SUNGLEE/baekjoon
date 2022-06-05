import sys
import heapq

N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
distances = [sys.maxsize for _ in range(N+1)]
heap = []

for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    arr[start].append([end, cost])

start, end = map(int, sys.stdin.readline().split())

#dijkstra
distances[start] = 0
heapq.heappush(heap, [distances[start], start])

while heap:
    v1Distance, v1 = heapq.heappop(heap)

    if v1Distance > distances[v1]:
        continue

    for v2, v2Distance in arr[v1]:
        distance = v1Distance + v2Distance

        if distance < distances[v2]:
            distances[v2] = distance
            heapq.heappush(heap, [distance, v2])

print(distances[end])