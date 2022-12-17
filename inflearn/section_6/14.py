# 14. 인접 행렬 (가중치 방향 그래프)

import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N, M = map(int, input().split())
    g=[[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        i, j, cost = map(int,input().split())
        g[i][j] = cost
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(g[i][j], end=" ")
        print()