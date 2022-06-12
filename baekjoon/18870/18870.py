n = int(input())

arr = list(map(int, input().split()))

sortedArr = sorted(arr)
tmp = sortedArr[0]
X = 0
dic = dict()
dic[sortedArr[0]] = 0

for i in range(1,n):
    if sortedArr[i] == tmp:
        continue

    else:
        X += 1
        dic[sortedArr[i]] = X
        tmp = sortedArr[i]

for i in range(n):
    print(dic[arr[i]], end=" ")