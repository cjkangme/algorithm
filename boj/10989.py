#10989. 수 정렬하기 3

import sys
input = sys.stdin.readline

T = int(input())

count_list = [0] * 10001 # 최대값이 10,000보다 작거나 같다
for num in range(T):
    count_list[int(input())] += 1

for i in range(1, len(count_list)):
    count_list[i] += count_list[i-1]

for i in range(len(count_list[i])):
    if i == 0:
        for _ in range(count_list[i]):
            print(i)
    for _ in range(count_list[i-1], count_list[i]):
        print(i)