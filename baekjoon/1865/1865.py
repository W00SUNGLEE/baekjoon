import sys
from collections import defaultdict

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())

    graph = defaultdict(lambda: defaultdict(lambda: sys.maxsize))

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())

        if t < graph[s][e]:
            graph[s][e] = t

        if t < graph[e][s]:
            graph[e][s] = t

    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        if -t < graph[s][e]:
            graph[s][e] = -t

    distance = [sys.maxsize for _ in range(n+1)]
    distance[1] = 0

    for i in range(n-1):
        for node in graph:
            for neighbor in graph[node]:
                if distance[node] + graph[node][neighbor] < distance[neighbor]:
                    distance[neighbor] = distance[node] + graph[node][neighbor]

    answer = False

    for node in graph:
        for neighbor in graph[node]:
            if distance[node] + graph[node][neighbor] < distance[neighbor]:
                answer = True

            if answer:
                break

        if answer:
            break

    if answer:
        print("YES")

    else:
        print("NO")
