import sys

n, m, k = map(int, sys.stdin.readline().split())

graph = list()

for _ in range(n):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp_list[1:])

selected = [-1 for _ in range(m+1)]

def bimatch(index):
    if visited[index]:
        return False

    visited[index] = True

    for num in graph[index]:
        if selected[num] == -1 or bimatch(selected[num]):
            selected[num] = index
            return True

    return False

answer = 0
for i in range(n):
    visited = [False for _ in range(n)]
    if bimatch(i):
        answer += 1

for i in range(n):
    visited = [False for _ in range(n)]
    if bimatch(i):
        answer += 1
        k -= 1
        if k == 0:
            break

print(answer)
