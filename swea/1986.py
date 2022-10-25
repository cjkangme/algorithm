#1986. 지그재그 숫자 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1986.txt", "r")

test_case = int(input())

for T in range(1, test_case+1):
    num = int(input())
    sum = 0
    for N in range(1, num+1):
        if N % 2 == 1:
            sum += N
        else:
            sum -= N
    print(f'#{T} {sum}')