import sys

n0 = [1, 0, 1]
n1 = [0, 1, 1]

def fibonacci(n):
  length = len(n0)
  if n >= length:
    for i in range(length, n+1):
      n0.append(n0[i-2]+n0[i-1])
      n1.append(n1[i-2]+n1[i-1])
      
n = int(sys.stdin.readline())

for i in range(n):
  tmp = int(sys.stdin.readline())
  fibonacci(tmp)
  print(n0[tmp], n1[tmp])