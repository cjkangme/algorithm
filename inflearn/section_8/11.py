# 11. 최대 점수 구하기 (냅색 알고리즘)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N, M = map(int,input().split())
    dy = [[0 for _ in range(M+1)] for _ in range(2)]
    for _ in range(1, N+1):
        score, time = map(int,input().split())
        for j in range(time, M+1):
            dy[1][j] = max(dy[0][j-time] + score, dy[0][j])
        for i in range(M+1):
            dy[0][i] = dy[1][i]
    print(dy[1][M])