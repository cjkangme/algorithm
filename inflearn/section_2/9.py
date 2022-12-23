# 9. 주사위 게임

import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

N = int(input())
answer = -1
for _ in range(N):
    tmp = input().split() # 문자화된 숫자가 리스트로 들어간다.
    tmp.sort()
    a, b, c = map(int, tmp)
    if a==b and b==c:
        price = 10000 + a * 1000
    elif a==b or a==c:
        price = 1000 + a * 100
    elif b==c:
        price = 1000 + b * 100
    else:
        price = a * 100
    if price > answer:
        answer = price
print(answer)