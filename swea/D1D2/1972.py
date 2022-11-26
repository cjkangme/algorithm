# 1979. 어디에 단어가 들어갈 수 있을까 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1972.txt", 'r')

test_case = int(input())

for T in range(1, test_case+1):
    N, K = map(int, input().split())
    puzzle = list(range(N))
    for i in range(N):
        puzzle[i] = [*map(int, input().split())]
    answer = 0
    # 가로 탐색
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 0:
                if count == K:
                    answer += 1
                count = 0
            else:
                count += 1
        if count == K:
            answer += 1
    # 세로 탐색
    for j in range(N):
        count = 0
        for i in range(N):
            if puzzle[i][j] == 0:
                if count == K:
                    answer += 1
                count = 0
            else:
                count += 1
        if count == K:
            answer += 1
    print(f'#{T} {answer}')
                

