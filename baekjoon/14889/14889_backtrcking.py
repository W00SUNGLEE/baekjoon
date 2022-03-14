import sys

arr = []
n = int(sys.stdin.readline())
check = [0] * n
solution = sys.maxsize

for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))

def stat():
  stat_start = 0
  stat_link = 0
  for i in range(n):
    for j in range(i+1,n):
      if check[i] == 1 and check[j] == 1:
        stat_start = stat_start + arr[i][j] + arr[j][i]
      elif check[i] == 0 and check[j] == 0:
        stat_link = stat_link + arr[i][j] + arr[j][i]

  return abs(stat_start-stat_link)
  

def dfs(idx, x):
  global check
  global solution
  
  if idx == n/2:
    solution = min(solution, stat())
    return

  else:
    for i in range(x, n):
      if check[i] == 0:
        check[i] += 1
        dfs(idx + 1, i + 1)
        check[i] -= 1
  
dfs(0, 0)
print(solution)