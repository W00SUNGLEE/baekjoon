import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    q = int(sys.stdin.readline())

    min_heap = list()
    max_heap = list()
    dic = dict()

    for i in range(q):
        command = list(sys.stdin.readline().split())

        if command[0] == 'I':
            heapq.heappush(min_heap, (int(command[1]), i))
            heapq.heappush(max_heap, (-int(command[1]), i))
            dic[i] = True

        elif command[0] == 'D':
            if len(min_heap) == 0:
                continue

            else:
                if command[1] == '1':
                    while max_heap and not dic[max_heap[0][1]]:
                        heapq.heappop(max_heap)

                    if max_heap:
                        dic[max_heap[0][1]] = False
                        heapq.heappop(max_heap)


                elif command[1] == '-1':
                    while min_heap and not dic[min_heap[0][1]]:
                        heapq.heappop(min_heap)

                    if min_heap:
                        dic[min_heap[0][1]] = False
                        heapq.heappop(min_heap)

    while max_heap and not dic[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not dic[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if len(max_heap) == 0:
        print("EMPTY")

    else:
        print(-(heapq.heappop(max_heap)[0]), heapq.heappop(min_heap)[0])