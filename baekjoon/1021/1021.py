import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

queue = deque([i for i in range(1, n+1)])

popIndex = list(map(int, sys.stdin.readline().split()))

answer = 0

for i in range(len(popIndex)):
    count = 0

    while True:
        if queue[0] == popIndex[i]:
            answer += min(count, len(queue) - count)
            queue.popleft()
            break

        else:
            queue.append(queue.popleft())
            count += 1

print(answer)