import sys
from collections import defaultdict

n = int(input())
answer = n

for i in range(n):
    string = sys.stdin.readline()

    alpha = defaultdict(int)

    for j in range(len(string)):
        if j == 0:
            tmp = string[j]

        else: #j > 0
            if string[j] == tmp:
                continue
            elif string[j] != tmp:
                if string[j] in alpha.keys():
                    answer -= 1
                    break
                alpha[tmp] += 1
                tmp = string[j]

print(answer)


