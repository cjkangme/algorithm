# 10. 점수계산

import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
score = 1
answer = 0
for n in lst:
    if n == 0:
        score = 1
    else:
        answer += score
        score += 1
print(answer)
