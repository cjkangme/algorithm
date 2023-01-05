# 12. 단지 번호 붙이기 (DFS)

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(x, y):
    global cnt
    if house[x][y] == 0:
        return
    else:
        house[x][y] = 0
        cnt += 1
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<N and 0<=yy<N:
                DFS(xx, yy)

if __name__=="__main__":
    N = int(input())
    house = [list(map(int,input().rstrip())) for _ in range(N)]
    cnt_list = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            cnt = 0
            if house[i][j] == 1:
                DFS(i, j)
            if cnt:
                cnt_list.append(cnt)
    cnt_list.sort()
    print(len(cnt_list))
    for num in cnt_list:
        print(num)