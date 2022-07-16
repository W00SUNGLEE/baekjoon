import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

circle = deque([i for i in range(1, n+1)])
answer = list()

while len(circle) != 0:
    for _ in range(k-1):
        circle.append(circle.popleft())

    answer.append(circle.popleft())

print("<", end="")
for i in range(n-1):
    print(str(answer[i])+",", end=" ")
print(str(answer[n-1]), end="")
print(">", end="")