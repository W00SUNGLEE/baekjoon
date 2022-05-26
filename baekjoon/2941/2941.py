import sys

string = sys.stdin.readline().strip()

n = len(string)
i = n-1

answer = n

while i >= 0:
    if string[i]== "=":
        i -= 1
        if string[i] == "c":
            i -= 1
            answer -= 1

        elif string[i] == "z":
            i -= 1
            answer -= 1

            if string[i] == "d":
                i -= 1
                answer -= 1

        elif string[i] == "s":
            i -= 1
            answer -= 1

    elif string[i] == "-":
        i -= 1
        if string[i] == "c":
            i -= 1
            answer -= 1

        elif string[i] == "d":
            i -= 1
            answer -= 1

    elif string[i] == "j":
        i -= 1
        if string[i] == "l":
            i -= 1
            answer -= 1

        elif string[i] == "n":
            i -= 1
            answer -= 1

    else:
        i -= 1

print(answer)