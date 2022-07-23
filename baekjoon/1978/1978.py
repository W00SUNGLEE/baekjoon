import sys

# 에라토스테네스의 체
primeList = [True for _ in range(1001)]
primeList[1] = False # 1은 소수 x

for i in range(2, 1001):
    if primeList[i] == False:  # i 보다 작은 값으로 나누어짐(소수 x)
        continue

    else:  # primeList[i] == True: # i 보다 작은 값으로 나누어지지않음(소수)
        for j in range(i * 2, 1001, i):
            primeList[j] = False

# 데이터 입력
n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

answer = 0

for number in numbers:
    if primeList[number]:
        answer += 1

print(answer)