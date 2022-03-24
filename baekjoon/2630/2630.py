import sys

arr = []
solution = [0, 0]

n = int(sys.stdin.readline())

for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().split())))

def func(x, y, n):
  for i in range(n):
    for j in range(n):
      if arr[x+i][y+j] != arr[x][y]:
        func(x, y, n//2)
        func(x, y+n//2, n//2)
        func(x+n//2, y, n//2)
        func(x+n//2, y+n//2, n//2)
        return None

  solution[arr[x][y]] += 1

func(0, 0, n)

print(solution[0])
print(solution[1])