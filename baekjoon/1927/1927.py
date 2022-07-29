import sys
import heapq

heap = list()

n = int(sys.stdin.readline())

for _ in range(n):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        if len(heap) == 0:
            print(0)

        else:
            print(heapq.heappop(heap))

    else:
        heapq.heappush(heap, tmp)