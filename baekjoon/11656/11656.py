import sys

answers = list()

S = list(sys.stdin.readline().strip())

for i in range(len(S)):
    answers.append("".join(S[i:len(S)]))

answers.sort()

for answer in answers:
    print(answer)