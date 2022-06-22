import sys

arr = sys.stdin.readline().strip()
n = len(arr)
dic = dict()

for i in range(n):
    for j in range(n-i):
        dic[arr[j:j+i+1]] = 1

print(len(dic.keys()))