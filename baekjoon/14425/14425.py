import sys
from collections import defaultdict

n, m = map(int, input().split())

S = defaultdict(int)

for _ in range(n):
    S[sys.stdin.readline()] = 1

answer = 0

for _ in range(m):
    if S[sys.stdin.readline()] == 1:
        answer += 1

print(answer)