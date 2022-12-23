# 4. 대표값

import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

N = int(input())
students = [*map(int,input().split())]
avg = int((sum(students) / N) + 0.5)
answer = 0
least = float('inf')

for idx, score in enumerate(students):
    temp = abs(score - avg)
    if temp < least:
        least = temp
        answer = idx+1
    elif temp == least:
        if students[answer-1] < score:
            answer = idx+1

print(f'{avg} {answer}')