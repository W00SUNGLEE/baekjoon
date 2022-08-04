n, k = map(int, input().split())

arr = list()
arr.append([1])
tmpList = list()

for i in range(1, n+1):
    tmpList.clear()

    for j in range(0, i+1):
        if j == 0 or j == i:
            tmpList.append(1)

        else:
            tmp = arr[i-1][j-1] + arr[i-1][j]

            if tmp >= 10007:
                tmp -= 10007

            tmpList.append(tmp)

    arr.append(tmpList.copy())

print(arr[n][k])
