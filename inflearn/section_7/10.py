# 미로 탐색(DFS)

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(x, y):
    global cnt
    if x==6 and y==6:
        cnt += 1
        return
    else:
        for i in range(4):
            go_x = x+dx[i]
            go_y = y+dy[i]
            if 0<=go_x<=6 and 0<=go_y<=6 and maze[go_y][go_x] == 0:
                maze[go_y][go_x] = 1
                DFS(go_x, go_y)
                maze[go_y][go_x] = 0

if __name__=="__main__":
    maze = [list(map(int,input().split())) for _ in range(7)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cnt = 0
    maze[0][0] = 1
    DFS(0,0)
    print(cnt)