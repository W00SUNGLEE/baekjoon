import sys

n = int(sys.stdin.readline())

stack = list()
pushIndex = 1
answer = list()

for _ in range(1, n+1):
    tmp = int(sys.stdin.readline())

    while True:
        if len(stack) == 0:
            stack.append(pushIndex)
            answer.append("+")
            pushIndex += 1

        else:
            if stack[len(stack)-1] == tmp:
                stack.pop()
                answer.append("-")
                break

            elif stack[len(stack)-1] < tmp:
                stack.append(pushIndex)
                answer.append("+")
                pushIndex += 1

            else: # stack[len(stack)-1] > i:
                answer = ["NO"]
                break

    if answer[0] == "NO":
        break

for string in answer:
    print(string)