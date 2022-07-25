import sys

string = list(sys.stdin.readline().strip())

count = 1

for i in range(1, len(string)):
    if string[i] != string[i-1]:
        count += 1

    else:
        continue

print(count//2)