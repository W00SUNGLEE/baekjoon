import sys
from collections import deque

queue = deque(list())

n = int(sys.stdin.readline())

def push(X):
    queue.append(X)

def pop():
    if len(queue) == 0:
        print(-1)

    else:
        print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)

    else:
        print(0)

def front():
    if len(queue) == 0:
        print(-1)

    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)

    else:
        print(queue[len(queue)-1])

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        push(command[1])

    elif command[0] == "pop":
        pop()

    elif command[0] == "size":
        size()

    elif command[0] == "empty":
        empty()

    elif command[0] == "front":
        front()

    elif command[0] == "back":
        back()