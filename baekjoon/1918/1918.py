import sys

string = sys.stdin.readline()

stack = list()
answer = list()

for i in range(len(string)):
    if string[i].isalpha():
        answer.append(string[i])

    else:
        if string[i] == '(':
            stack.append(string[i])

        elif string[i] == '*' or string[i] == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer.append(stack.pop())

            stack.append(string[i])

        elif string[i] == '+' or string[i] == '-':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())

            stack.append(string[i])

        elif string[i] == ')':
            while stack and stack[-1] != '(':
                answer.append(stack.pop())

            stack.pop()

while stack:
    answer.append(stack.pop())

print(''.join(map(str, answer)))
