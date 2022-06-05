import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
distances = [sys.maxsize for _ in range(N+1)]
heap = []
saveDistance = []
answer = 0


for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    arr[start].append([end, cost])

def dijkstra(X: int):
    distances = [sys.maxsize for _ in range(N + 1)]
    heap = []

    distances[0] = 0
    distances[X] = 0
    heapq.heappush(heap, [0, X])

    while heap:
        v1Distance, v1 = heapq.heappop(heap)

        if v1Distance > distances[v1]:
            continue

        for v2, v2Distance in arr[v1]:
            distance = v1Distance + v2Distance

            if distance < distances[v2]:
                distances[v2] = distance
                heapq.heappush(heap, [distance, v2])

    saveDistance.append(distances)

for i in range(1,N+1):
    dijkstra(i)

for i in range(1, N+1):
    answer = max(saveDistance[X-1][i]+saveDistance[i-1][X], answer)

print(answer)
