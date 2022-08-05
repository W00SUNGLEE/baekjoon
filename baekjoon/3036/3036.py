import sys

n = int(sys.stdin.readline())

rings = list(map(int, sys.stdin.readline().split()))

def Euclidean(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for i in range(1, n):
    if rings[0] > rings[i]:
        gcd = Euclidean(rings[0], rings[i])

    else:
        gcd = Euclidean(rings[i], rings[0])

    print("{}/{}".format(rings[0] // gcd, rings[i] // gcd))