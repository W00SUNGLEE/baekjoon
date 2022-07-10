import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque(list())
for _ in range(n):
    parenthesis = sys.stdin.readline().strip()

    answer = "YES"
    stack.clear()
    for i in range(len(parenthesis)):
        if parenthesis[i] == "(":
            stack.append("(")

        else: # parenthesis[i] == ")":
            if len(stack) < 1:
                answer = "NO"
                break

            else:
                stack.pop()

    if len(stack) > 0:
        answer = "NO"

    print(answer)