# 섬나라 아일랜드(BFS 활용)

import sys
from collections import deque
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    map = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1] # 12시부터 시계 방향
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    que = deque()
    for i in range(N):
        for j in range(N):
            if map[i][j] == 1:
                map[i][j] = 0
                que.append((i,j))
                while que:
                    x, y = que.popleft()
                    for k in range(8):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<N and 0<=yy<N and map[xx][yy] == 1:
                            map[xx][yy] = 0
                            que.append((xx, yy))
                cnt += 1
    print(cnt)