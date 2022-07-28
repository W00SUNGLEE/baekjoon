import sys

S = sys.stdin.readline().strip()

answer = list()
tmp = list()
i = 0

while i < len(S):
    if S[i] == "<":
        while S[i] != ">":
            tmp.append(S[i])
            i += 1

        tmp.append(S[i])
        i += 1

        answer.append("".join(tmp))

    elif S[i] == " ":
        answer.append(S[i])
        i += 1

    else:
        while i < len(S):
            if S[i] == "<":
                answer.append("".join(tmp[::-1]))
                break

            elif S[i] == " ":
                answer.append("".join(tmp[::-1]))
                answer.append(" ")
                i += 1
                break

            tmp.append(S[i])
            i += 1

        if i == len(S):
            answer.append("".join(tmp[::-1]))

    tmp.clear()

print("".join(answer))