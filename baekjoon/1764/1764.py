import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

dic = defaultdict(int)

for i in range(n):
    dic[sys.stdin.readline().strip()] = 1

answer = list()
count = 0

for i in range(m):
    person = sys.stdin.readline().strip()
    if dic[person] == 1:
        answer.append(person)
        count += 1

answer.sort()

print(count)
for i in range(len(answer)):
    print(answer[i])