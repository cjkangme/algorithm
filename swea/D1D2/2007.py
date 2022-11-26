#2007. 패턴 마디의 길이 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\2007.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    text = input()
    word = [text[0]]
    for i in range(len(text)-1):
        if text[0] != text[i+1]:
            word.append(text[i+1])
        elif text[0] == text[i+1]:
            if text[:i] == text[i + 1 : i + len(word)] and text[:i] == text[i + len(word) + 1 : i + len(word) + len(word)]:
                print(f'#{test_case} {len(word)}')
                break
            else:
                word.append(text[i+1])
    

