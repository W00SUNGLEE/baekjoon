#import sys
#sys.setrecursionlimit(10000)

A, B, C = map(int, input().split())

def recursive(b):
    if b == 1:
        return A % C

    else:
        if b % 2 == 0:
            return (recursive(b//2) ** 2) % C
        else:
            return (recursive(b//2) ** 2 * A) % C

print(recursive(B))

"""
arr = []
while B != 2:
    if B % 2 == 1:
        arr.append(A)
    else:
        arr.append(1)
    B = B // 2

tmp = A**2

for i in range(C):
    if (tmp - i) % C == 0:
        break

while arr:
    tmp = (i ** 2) * arr.pop()
    for i in range(C):
        if (tmp - i) % C == 0:
            break

print(i)
"""