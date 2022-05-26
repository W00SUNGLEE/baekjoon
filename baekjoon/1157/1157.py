import sys
from collections import defaultdict

string = str(sys.stdin.readline().strip())

n = len(string)

dic = defaultdict(int)

for i in range(n):
    if string[i].islower():
        dic[string[i].upper()] += 1
    else: #isupper()
        dic[string[i]] += 1

count = 0
for key, value in dic.items():
    if value > count:
        count = value
        answer = key

    elif value == count:
        answer = "?"

    else:
        continue

print(answer)