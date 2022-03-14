import sys

arr = []
blank = []

for i in range(9):
  arr.append(list(map(int,sys.stdin.readline().split())))

for i in range(9):
  for j in range(9):
    if arr[i][j] == 0:
      blank.append([i, j])

def promisingRow(x, a):
  for i in range(9):
    if arr[x][i] == a:
      return False
  return True
  
def promisingCol(y, a):
  for i in range(9):
    if arr[i][y] == a:
      return False
  return True

def promisingSqu(x, y, a):
  for i in range((x//3)*3,(x//3)*3+3):
    for j in range((y//3)*3,(y//3)*3+3):
      if arr[i][j] == a:
        return False
  return True

def sudoku(v):  
  if v == len(blank):
    for i in range(9):
      print(*arr[i])
    exit(0)

  for i in range(1, 10):
    x = blank[v][0]
    y = blank[v][1]

    if promisingRow(x, i) and promisingCol(y, i) and promisingSqu(x, y, i):
      arr[x][y] = i
      sudoku(v+1)
      arr[x][y] = 0
    
sudoku(0)