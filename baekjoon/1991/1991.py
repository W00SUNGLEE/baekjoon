import sys
from collections import defaultdict

dic = defaultdict(list)

n = int(sys.stdin.readline())

for i in range(n):
    a, b, c = sys.stdin.readline().split()

    dic[a].append(b)
    dic[a].append(c)

def prefix(index):
    print(index, end='')

    if dic[index][0] != '.':
        prefix(dic[index][0])

    if dic[index][1] != '.':
        prefix(dic[index][1])

def infix(index):
    if dic[index][0] != '.':
        infix(dic[index][0])

    print(index, end='')

    if dic[index][1] != '.':
        infix(dic[index][1])

def postfix(index):
    if dic[index][0] != '.':
        postfix(dic[index][0])

    if dic[index][1] != '.':
        postfix(dic[index][1])

    print(index, end='')

prefix('A')
print()
infix('A')
print()
postfix('A')
print()
