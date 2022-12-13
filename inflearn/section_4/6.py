# 6. 씨름 선수 (그리디)
import sys
sys.stdin=open("inflearn/section_4/input.txt", "r")

N = int(input())
lst = list(range(N))
for i in range(N):
    lst[i] = [*map(int, input().split())]
lst.sort(reverse=True)
cnt = 1
max_w = 0
for i in range(N):
    if i == 0:
        max_w = lst[i][1]
        continue
    if lst[i][1] > max_w:
        max_w = lst[i][1]
        cnt += 1
print(cnt)
        
