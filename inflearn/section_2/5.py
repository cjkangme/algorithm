# 5. 정다면체

import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

N, M = map(int,input().split())
count_list = [0] * (N+M+1)
for i in range(1, N+1):
    for j in range(1, M+1):
        count_list[i+j] += 1

max_num = max(count_list)
for idx, value in enumerate(count_list):
    if value == max_num:
        print(idx, end=" ")