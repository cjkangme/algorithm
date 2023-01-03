# 등산 경로(DFS)

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(x,y):
    global cnt
    if x==end[1] and y==end[0]:
        cnt += 1
        return
    else:
        for j in range(4):
            xx = x + dx[j]
            yy = y + dy[j]
            if 0<=xx<=N-1 and 0<=yy<=N-1 and path[yy][xx] > path[y][x]:
                temp = path[y][x]
                path[y][x] = MIN_NUM
                DFS(xx,yy)
                path[y][x] = temp

if __name__=="__main__":
    N = int(input())
    path = [list(map(int, input().split())) for _ in range(N)]
    path_min = 2147000000
    path_max = -2147000000
    start = [0, 0]
    end = [0, 0]
    for i in range(N):
        for j in range(N):
            if path[i][j] < path_min:
                path_min = path[i][j]
                start = [i, j]
            if path[i][j] > path_max:
                path_max = path[i][j]
                end = [i, j]
    MIN_NUM = -2147000000
    path[0][0] = MIN_NUM
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cnt = 0
    DFS(start[1], start[0])
    print(cnt)