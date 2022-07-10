import sys
from collections import deque

n = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

deq = deque(list())
answer = [-1 for _ in range(n)]

deq.append((0, (A[0])))

for i in range(1, n):
    Ai = A[i]

    for _ in range(len(deq)):
        j, Aj = deq.pop()

        if Ai > Aj:
            answer[j] = Ai
        else:
            deq.append((j, Aj))
            break

    deq.append((i, Ai))

for neg in answer:
    print(neg, end=" ")