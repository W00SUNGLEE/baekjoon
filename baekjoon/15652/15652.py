import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
arr = [i for i in range(1,n+1)]

solution = list(itertools.combinations_with_replacement(arr, m))

for i in range(len(solution)):
  for j in range(m):
    print(solution[i][j], end=" ")
  print("")