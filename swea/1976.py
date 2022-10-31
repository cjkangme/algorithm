# 1976. 시각 덧셈 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1976.txt", "r")

test_case = int(input())

for T in range(1, test_case+1):
    h1, m1, h2, m2 = [*map(int, input().split())]
    h = h1 + h2
    m = m1 + m2
    if m >= 60:
        h += m // 60
        m = m % 60
    if h >= 12:
        h -= 12
    print(f'#{T} {h} {m}')