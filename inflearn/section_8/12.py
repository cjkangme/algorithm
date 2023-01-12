# 12. 플로이드-와샬 (그래프 최단거리)

import sys
sys.stdin = open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    MAX_NUM = 2147000000
    dis = [[MAX_NUM] * N for _ in range(M)]
    for _ in range(M):
        i, j, value = map(int, input().split())
        dis[i-1][j-1] = value
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    dis[i][j] = 0
                    continue
                else:
                    dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])
    for i in range(N):
        for j in range(N):
            if dis[i][j] == MAX_NUM:
                print("M", end=" ")
            else:
                print(dis[i][j], end=" ")
        print()
