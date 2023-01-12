# 13. 회장뽑기(플로이드-워샬 응용)

import sys
sys.stdin = open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

MAX_NUM = 214700000

if __name__=="__main__":
    N = int(input())
    dis = [[MAX_NUM]*N for _ in range(N)]
    score_list = [0] * N
    while True:
        x, y = map(int,input().split())
        if x==-1 and y==-1:
            break
        dis[x-1][y-1] = 1
        dis[y-1][x-1] = 1
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
    for i in range(N):
        score_list[i] = max(dis[i])
    min_score = min(score_list)
    print(f'{min_score} {score_list.count(min_score)}')
    for i in range(N):
        if score_list[i] == min_score:
            print(i+1, end=" ")