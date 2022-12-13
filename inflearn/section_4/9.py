import sys
from collections import deque
sys.stdin=open("inflearn/section_4/input.txt", "r")

N = int(input())
lst = [*map(int,input().split())]

last = 0
i = 0
j = N - 1
cnt = 0
char = []

while i < j:
    lt = (lst[i], "L")
    rt = (lst[j], "R")
    if lt[0] <= last and rt[0] <= last:
        break
    elif (lt[0] > last and lt[0] <= rt[0]) or rt[0] <= last:
        last = lt[0]
        cnt += 1
        i += 1
        char.append(lt[1])
    elif (rt[0] > last and lt[0] > rt[0]) or lt[0] <= last:
        last = rt[0]
        cnt += 1
        j -= 1
        char.append(rt[1])

if lst[i] > last:
    cnt += 1
    char.append("L")

print(cnt)
for c in char:
    print(c, end="")