import sys

n = int(sys.stdin.readline())

prim_list = [True for i in range(2001)]

prim_list[0] = False
prim_list[1] = False

for i in range(2, 45):
    if prim_list[i] == True:
        for j in range(2*i, 2001, i):
            prim_list[j] = False

first_list = list()
second_list = list()

tmp_list = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if tmp_list[0] % 2 == tmp_list[i] % 2:
        first_list.append(tmp_list[i])

    else:
        second_list.append(tmp_list[i])

def bimatch(index):
    if visited[index]:
        return False

    visited[index] = True

    for num in graph[index]:
        if selected[num] == -1 or bimatch(selected[num]):
            selected[num] = index
            return True

    return False

graph = [[] for _ in range(len(first_list))]

for i in range(len(first_list)):
    for j in range(len(second_list)):
        if prim_list[first_list[i] + second_list[j]]:
            graph[i].append(j)

answer = list()

for i in graph[0]:
    selected = [-1 for _ in range(len(second_list))]
    selected[i] = 0
    count = 1

    for j in range(len(first_list)):
        visited = [False for _ in range(len(first_list))]
        visited[0] = True

        if bimatch(j):
            count += 1

    if count == n // 2:
        answer.append(second_list[i])

if answer:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i], end=" ")

else:
    print(-1)
