import sys
from collections import deque

queue = deque(list())

t = int(sys.stdin.readline())

for _ in range(t):
    answer = 0
    queue.clear()
    prioritys = [0 for _ in range(10)]

    n, m = map(int, sys.stdin.readline().split())
    tmp = list(map(int, sys.stdin.readline().split()))

    for i in range(n):
        queue.append((i, tmp[i]))
        prioritys[tmp[i]] += 1

    while len(queue) > 0:
        index, priority = queue.popleft()

        haveHighPriority = False

        for i in range(priority+1, 10):
            if prioritys[i] > 0:

                haveHighPriority = True
                break

        if haveHighPriority:
            queue.append((index, priority))

        else:
            answer += 1
            prioritys[priority] -= 1

            if index == m:
                print(answer)
                break