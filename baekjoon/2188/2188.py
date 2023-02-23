import sys

n, m = map(int, sys.stdin.readline().split())

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

for i in range(n):
    visited = [False for _ in range(n)]
    bimatch(i)

answer = 0

for i in range(1, m+1):
    if selected[i] >= 0:
        answer += 1

print(answer)