import sys

arr = [0, 1, 2]

def func(n):  
  if n >= len(arr):
    for i in range(len(arr), n+1):
      arr.append((arr[i-2] + arr[i-1])%15746)
      
n = int(sys.stdin.readline())

func(n)

print(arr[n])