#1989. 초심자의 회문 검사 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1989.txt", "r")

test_case = int(input())

for T in range (1, test_case+1):
    text = input()
    reverse = list(range(len(text)))
    for i in reverse:
        reverse[i] = text[len(text)-(i+1)]
    if ''.join(reverse)==text:
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')
