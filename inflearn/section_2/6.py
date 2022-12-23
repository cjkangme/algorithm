# 6. 자릿수의 합

import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

def digit_sum(x):
    tmp = 0
    for c in str(x):
        tmp += int(c)
    return tmp

N = int(input())
lst = [*map(int, input().split())]
max_num = 0
answer = -1

for n in lst:
    total = digit_sum(n)
    if total > max_num:
        max_num = total
        answer = n
print(answer)

