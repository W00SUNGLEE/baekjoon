import sys
import itertools

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operater = list(map(int, sys.stdin.readline().split()))

arr = []
per_arr = []
solution = []

for i in range(4):
  for j in range(operater[i]):
    arr.append(i)

per_arr = list(itertools.permutations(arr))

def operate(a, b, x):
  if x == 0:
    return a + b
  elif x == 1:
    return a - b
  elif x == 2:
    return a * b
  elif x == 3:
    if a * b >=0:
      return a // b
    else:
      return (abs(a) // abs(b) * (-1))


for i in range(len(per_arr)):
  tmp = int(A[0])

  for j in range(1,n):
    tmp = operate(tmp, A[j], per_arr[i][j-1])
  solution.append(tmp)

print(max(solution))
print(min(solution))