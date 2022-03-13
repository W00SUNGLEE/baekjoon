n = int(input())
arr = []
i = 666
cnt = 0
while True:
  arr = list(str(i))
  for j in range(0,len(arr)-2):
    if arr[j] == '6' and arr[j+1] == '6' and arr[j+2] == '6':
      cnt +=1
      break
      
  if n == cnt:
    print(i)
    break
    
  i += 1