# 14. 안전영역 (DFS)

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def DFS(x, y, h):
    chk[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<N and 0<=yy<N and board[xx][yy] > h and chk[xx][yy] == 0:
            DFS(xx, yy, h)

if __name__=="__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for height in range(1, 100):
        cnt = 0
        chk = [[0 for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if chk[x][y] == 0 and board[x][y] > height:
                    DFS(x, y, height)
                    cnt += 1
        max_cnt = max(max_cnt, cnt)
        if cnt == 0:
            break
    print(max_cnt)