#1983. 조교의 성적 매기기 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1983.txt", "r")

test_case = int(input())

for T in range(1, test_case+1):
    N, K = map(int,input().split())
    score = list(range(N))
    rank = 1

    for i in score:
        score[i] = [*map(int, input().split())]
        total_score = (score[i][0] * 35 + score[i][1] * 45 + score[i][2] * 20) / 100
        score[i].append(total_score)
        
    for i in range(N):
        if score[K-1][3] < score[i][3]:
            rank += 1
    if rank <= N // 10:
        print(f'#{T} A+')
    elif rank <= (N // 10) * 2:
        print(f'#{T} A0')
    elif rank <= (N // 10) * 3:
        print(f'#{T} A-')
    elif rank <= (N // 10) * 4:
        print(f'#{T} B+')
    elif rank <= (N // 10) * 5:
        print(f'#{T} B0')
    elif rank <= (N // 10) * 6:
        print(f'#{T} B-')
    elif rank <= (N // 10) * 7:
        print(f'#{T} C+')
    elif rank <= (N // 10) * 8:
        print(f'#{T} C0')
    elif rank <= (N // 10) * 9:
        print(f'#{T} C-')
    else:
        print(f'#{T} D0')
