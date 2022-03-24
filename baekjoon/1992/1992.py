import sys

arr = []

n = int(sys.stdin.readline())

for i in range(n):
  arr.append(list(map(int, list(sys.stdin.readline().strip()))))

def func(x, y, n):
  for i in range(n):
    for j in range(n):
      if arr[x+i][y+j] != arr[x][y]:
        print("(", end="")
        func(x, y, n//2)
        func(x, y+n//2, n//2)
        func(x+n//2, y, n//2)
        func(x+n//2, y+n//2, n//2)
        print(")", end="")
        return None

  print(arr[x][y], end="")

func(0, 0, n)
print()