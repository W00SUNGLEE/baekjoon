import sys
from collections import deque

def push_front(X):
    queue.appendleft(X)

def push_back(X):
    queue.append(X)

def pop_front():
    if len(queue) == 0:
        print(-1)

    else:
        print(queue.popleft())

def pop_back():
    if len(queue) == 0:
        print(-1)

    else:
        print(queue.pop())

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
        print(queue[-1])

queue = deque(list())

n = int(sys.stdin.readline())

for _ in range(n):
    command = list(map(str, sys.stdin.readline().split()))

    if command[0] == "push_front":
        push_front(int(command[1]))

    elif command[0] == "push_back":
        push_back(int(command[1]))

    elif command[0] == "pop_front":
        pop_front()

    elif command[0] == "pop_back":
        pop_back()

    elif command[0] == "size":
        size()

    elif command[0] == "empty":
        empty()

    elif command[0] == "front":
        front()

    elif command[0] == "back":
        back()