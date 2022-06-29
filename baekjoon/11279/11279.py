import sys
import heapq

n = int(sys.stdin.readline())
heapque = list()

for _ in range(n):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        if len(heapque) == 0:
            print(0)
        else:
            print(-heapq.heappop(heapque))

    else: # tmp != 0:
        heapq.heappush(heapque, -tmp)