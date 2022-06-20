import sys
import heapq

N, E = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a][b] = c
    matrix[b][a] = c

p1, p2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    distances = [sys.maxsize for _ in range(N+1)]
    heapQueue = list()
    distances[start] = 0

    heapq.heappush(heapQueue, (0, start))

    while heapQueue:
        d1, v1 = heapq.heappop(heapQueue)

        if d1 > distances[v1]:
            continue

        for i in range(1,N+1):
            if matrix[v1][i] > 0 and distances[v1]+matrix[v1][i] < distances[i]:
                distances[i] = distances[v1]+matrix[v1][i]
                heapq.heappush(heapQueue, (distances[i], i))

    return distances[end]

def twoPoint(p1, p2):
    a = dijkstra(1, p1)
    b = dijkstra(p1, p2)
    c = dijkstra(p2, N)

    if a == sys.maxsize or b == sys.maxsize or c == sys.maxsize:
        return sys.maxsize

    else:
        return a+b+c

answer = min(twoPoint(p1, p2), twoPoint(p2, p1))

if answer == sys.maxsize:
    print(-1)

else:
    print(answer)