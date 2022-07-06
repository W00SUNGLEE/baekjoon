import sys

string = sys.stdin.readline().strip()

number = list()
operator = list()

index = 0
for i in range(len(string)):
    if string[i] == '+' or string[i] == '-':
        operator.append(string[i])
        number.append(int(string[index:i]))
        index = i+1

number.append(int(string[index:]))

for i in range(len(operator)-1,-1,-1):
    if operator[i] == '+':
        number.insert(i, number.pop(i)+number.pop(i))

answer = number[0]

for i in range(1, len(number)):
    answer -= number[i]

print(answer)