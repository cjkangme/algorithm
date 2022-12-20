#17413. 단어 뒤집기
import sys
from collections import deque

input = sys.stdin.readline

string = input().rstrip()
deck = deque([])
cursor = 0
length = len(string)

while cursor < length:
    c = string[cursor]
    if c == "<":
        while string[cursor] != ">":
            deck.append(string[cursor])
            cursor += 1
        deck.append(string[cursor]) #">" 까지 출력해야하므로 한번 더 수행
        cursor += 1
        while deck:
            print(deck.popleft(), end="")
    elif c == " ":
        print(' ', end="")
        cursor += 1
    else:
        while string[cursor] != "<" and string[cursor] != ' ':
            deck.append(string[cursor])
            cursor += 1
            if cursor >= length:
                break
        while deck:
            print(deck.pop(), end="")