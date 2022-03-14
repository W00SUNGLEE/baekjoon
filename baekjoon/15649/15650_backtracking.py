n, m = map(int, input().split())

arr = [int(i) for i in range(1,n+1)]
check = [0] * n
solution_arr = [0] * m

def permuation(v):
  if v == m:
    print(*solution_arr)

  else:
    for i in range(n):
      if check[i] == 0 :
        solution_arr[v] = arr[i]
        check[i] += 1
        permuation(v+1)
        check[i] -= 1

permuation(0)