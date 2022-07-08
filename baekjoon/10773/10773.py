import sys

n = int(sys.stdin.readline())

stack = list()

for _ in range(n):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        stack.pop()

    else:
        stack.append(tmp)

print(sum(stack))