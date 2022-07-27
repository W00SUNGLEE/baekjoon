import sys

N = list(map(str, sys.stdin.readline().strip()))

N.sort(reverse=True)

if int(N[len(N)-1]) != 0:
    print(-1)

else:
    count = 0

    for i in range(len(N)):
        count += int(N[i])

    if count % 3 == 0:
        print("".join(N))

    else:
        print(-1)