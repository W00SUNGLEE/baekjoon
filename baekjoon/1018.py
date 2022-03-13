import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))

solution = 64

for a in range(n-7):
    for b in range(m-7):
      
        cnt = 0

        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] == 'W':
                      cnt += 1
                else:
                    if arr[i][j] == 'B':
                      cnt += 1
        
        if solution > min(cnt, 64-cnt):
          solution = min(cnt, 64-cnt)

print(solution)
