import sys

n, r, c = map(int, sys.stdin.readline().split())

answer = [0]

def recursive(n, r, c):
    length = 2**(n-1)

    if n == 0:
        return None

    if 0 <= r < length and 0 <= c < length:
        recursive(n-1, r, c)

    elif 0 <= r < length and length <= c < 2 * length:
        answer[0] += length**2
        recursive(n - 1, r, c - length)

    elif length <= r < 2 * length and 0 <= c < length:
        answer[0] += 2 * (length ** 2)
        recursive(n - 1, r - length, c)

    else:
        answer[0] += 3 * (length ** 2)
        recursive(n - 1, r - length, c - length)

recursive(n, r, c)
print(answer[0])