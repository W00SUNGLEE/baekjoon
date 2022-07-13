import sys

stack = list()

string = sys.stdin.readline()

while string[0] != '.':
    answer = 'yes'
    stack.clear()
    for a in string:
        if a == '(' or a == '[':
            stack.append(a)

        elif a == ')':
            if len(stack) > 0:
                tmp = stack.pop()
                if tmp == '(':
                    continue
                else:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break

        elif a == ']':
            if len(stack) > 0:
                tmp = stack.pop()
                if tmp == '[':
                    continue
                else:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break

    if len(stack) > 0:
        answer = 'no'

    print(answer)

    string = sys.stdin.readline()