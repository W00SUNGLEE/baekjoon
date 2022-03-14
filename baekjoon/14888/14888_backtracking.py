import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operater = list(map(int, sys.stdin.readline().split()))

numberOfOperater = n - 1

maxSolution = -1000000001
minSolution = 1000000001
check = [0] * 4
solution = [0] * n
solution[0] = A[0]

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

def dfs(v):
  global maxSolution
  global minSolution
  global solution
  if(numberOfOperater == v):
    maxSolution = max(maxSolution, solution[v])
    minSolution = min(minSolution, solution[v])
    return

  else:
    for i in range(4):
      if check[i] < operater[i]:
        check[i] += 1
        
        solution[v+1] = operate(solution[v], A[v+1], i)
        dfs(v+1)
        check[i] -= 1

dfs(0)
print(maxSolution)
print(minSolution)