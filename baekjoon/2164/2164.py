import sys
from collections import deque

n = int(sys.stdin.readline())

card = deque([i for i in range(n, 0, -1)])

while len(card) != 1:
    card.pop()
    card.appendleft(card.pop())

print(card.pop())