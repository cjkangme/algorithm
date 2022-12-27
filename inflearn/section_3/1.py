# 1. 회문 문자열 검사

import sys
sys.stdin=open("inflearn/section_3/input.txt", "r")
input = sys.stdin.readline

N = int(input())
for T in range(1,N+1):
    string = input().rstrip().lower()
    size = len(string)
    for i in range(size // 2):
        if string[i] != string[-1-i]:
            print(f"#{T} NO")
            break
    else: print(f"#{T} YES")