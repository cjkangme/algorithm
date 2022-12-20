# 10866. 덱
import sys
from collections import deque

def Deque(command):
    if command == "pop_front":
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif command == "pop_back":
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(deck))
    elif command == "empty":
        if deck:
            print(1)
        else:
            print(0)
    elif command == "front":
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif command == "back":
        if deck:
            print(deck[-1])
        else:
            print(-1)
    else:
        command, X = command.split()
        if command == "push_front":
            deck.appendleft(X)
        else:
            deck.append(X)

input = sys.stdin.readline

deck = deque([])

N = int(input())
for _ in range(N):
    Deque(input().rstrip())