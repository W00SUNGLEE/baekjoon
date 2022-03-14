import sys

n= int(sys.stdin.readline())
col = [0] * n
cnt = 0

def promising(i): 
  for k in range(i):
    if  (col[i] == col[k]) or abs(col[i]-col[k]) == abs(i-k):
      return False

  return True

def queens(i):
  global cnt
  if i == n:
    cnt += 1
  else:
    for j in range(n):
      col[i] = j
      if promising(i):
        queens(i+1)

queens(0)
print(cnt)