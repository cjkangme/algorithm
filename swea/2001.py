# 2001. 파리 퇴치 (D2)

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\2001.txt", "r")

def catch_fly(x, y, M):
    sum = 0
    for i in range(M):
        for j in range(M):
            sum += li[x + i][y + j]
    return sum

test_case = int(input())

for T in range(1, test_case + 1):
    # 배열 입력받기
    N, M = map(int, input().split())
    li = list(range(N))
    for i in range(N):
        li[i]= [*map(int, input().split())]

    # 구하기
    search_count = N - M + 1
    max = 0
    for i in range(search_count):
        for j in range(search_count):
            value = catch_fly(i, j, M)
            if value > max:
                max = value
    print(f'#{T} {max}')

