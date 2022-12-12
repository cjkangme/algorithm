#5. 회의실 배정
import sys
sys.stdin=open("inflearn/section_4/input.txt", "r")

N = int(input())
lst = list(range(N))
for i in range(N):
    lst[i] = [*map(int,input().split())]
time = 0
cnt = 0
lst.sort(key=lambda x : (x[1], x[0]))
for i in range(len(lst)):
    if lst[i][0] >= time:
        time = lst[i][1]
        cnt += 1
print(cnt)