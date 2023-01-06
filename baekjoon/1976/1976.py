import sys

sys.setrecursionlimit(10**6)

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

parent = [i for i in range(n)]

for i in range(n):
    tmp_list = list(map(int, sys.stdin.readline().split()))

    for j in range(n):
        if tmp_list[j] == 1:
            union(parent, i, j)

tmp_list = list(map(int, sys.stdin.readline().split()))

answer = "YES"
tmp = parent[tmp_list[0]-1]

for i in range(1, m):
    if parent[tmp_list[i]-1] != tmp:
        answer = "NO"
        break

print(answer)
