string = input()
arr = []

for i in range(len(string)):
    arr.append(int(string[i]))

arr.sort(reverse=False)
arr.reverse()

print("".join(list(list(map(str, arr)))))