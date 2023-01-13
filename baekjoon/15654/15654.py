import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())

number_list = list(map(int, sys.stdin.readline().split()))

number_list.sort()

for permutation in permutations(number_list, m):
    for number in permutation:
        print(number, end=' ')

    print()