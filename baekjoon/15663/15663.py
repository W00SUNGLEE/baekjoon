import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

number_list = list(map(int, sys.stdin.readline().split()))

number_list.sort()

for sequence in sorted(set(permutations(number_list, m))):
    for number in sequence:
        print(number, end=' ')
    print()
