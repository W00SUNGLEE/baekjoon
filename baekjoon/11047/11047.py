import sys

arr = []
cnt = 0
      
n, k = map(int, sys.stdin.readline().split())

for i in range(n):
  arr.append(int(sys.stdin.readline()))  

for i in reversed(range(n)):
  if k // arr[i]:
    cnt += k // arr[i]
    k = k % arr[i]
    
print(cnt)