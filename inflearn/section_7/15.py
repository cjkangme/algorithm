# 15. 토마토 (BFS 활용)

import sys
from collections import deque
# pyright: reportUnboundVariable=false
sys.stdin = open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    M, N = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dq = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                dq.append((i, j))

    while dq:
        x, y = dq.popleft()
        answer = board[x][y]
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < N and 0 <= yy < M and board[xx][yy] == 0:
                board[xx][yy] = answer + 1
                dq.append((xx, yy))
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                print(-1)
                sys.exit(0)
    print(answer-1)
