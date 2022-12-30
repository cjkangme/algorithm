# 11_2. 최대 점수 구하기 (냅색 알고리즘 + 1차원 배열)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N, M = map(int,input().split())
    dy = [0 for _ in range(M+1)]
    for _ in range(N):
        score, time = map(int,input().split())
        for i in range(M, time-1, -1):
            dy[i] = max(dy[i-time]+score, dy[i])
    print(dy[M])