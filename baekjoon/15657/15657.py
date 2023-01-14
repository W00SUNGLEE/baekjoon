import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())

number_list = list(map(int, sys.stdin.readline().split()))

number_list.sort()

for sequence in combinations_with_replacement(number_list, m):
    for number in sequence:
        print(number, end=' ')

    print()