import sys
import heapq

moves = [-1, 1, 2]

N, K = map(int, sys.stdin.readline().split())

cost = [sys.maxsize for _ in range(100001)]
heap = []

#dijkstra
cost[N] = 0
heapq.heappush(heap, (cost[N], N))

while heap:
    N1Cost, N1 = heapq.heappop(heap)

    if N1 == K:
        break

    if N1Cost > cost[N1]:
        continue

    for move in moves:
        if move == 2:
            tmpCost = N1Cost
            tmpIndex = N1 * move

        else: # -1 or 1:
            tmpCost = N1Cost + 1
            tmpIndex = N1 + move

        if 0 <= tmpIndex <= 100000 and tmpCost < cost[tmpIndex]:
            cost[tmpIndex] = tmpCost
            heapq.heappush(heap, (tmpCost, tmpIndex))

print(cost[K])