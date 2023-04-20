import sys

n, m = map(int, sys.stdin.readline().split())

tmp = list(map(int, sys.stdin.readline().split()))

parent = [i for i in range(n+1)]

for i in range(1, len(tmp)):
    parent[tmp[i]] = 0

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b

party_list = list()

for _ in range(m):
    tmp = list(map(int, sys.stdin.readline().split()))

    for i in range(1, len(tmp)-1):
        union(tmp[i], tmp[i+1])

    party_list.append(tmp)

answer = m

for i in range(len(party_list)):
    for j in range(1, len(party_list[i])):
        if find(party_list[i][j]) == 0:
            answer -= 1
            break

print(answer)
