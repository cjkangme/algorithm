# 미로의 최단거리 통로

import sys
from collections import deque
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    maze = [list(map(int,input().split())) for _ in range(7)]
    dis = [[0 for _ in range(7)] for _ in range(7)]
    maze[0][0] = 1 # 방문한 노드는 그냥 벽으로 친다.
    dq = deque() # 방문할 노드를 저장할 큐
    dq.append((0,0)) # 출발노드
    dx = [0, 1, 0, -1] # 12시, 3시, 6시, 9시 순 으로 방향을 지정하는 리스트 (x방향)
    dy = [-1, 0, 1, 0] # 12시, 3시, 6시, 9시 순 으로 방향을 지정하는 리스트 (y방향)
    while dq: # 더이상 방문할 곳이 없으면 멈춤
        temp = dq.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if 0 <= x <= 6 and 0 <= y <= 6 and maze[x][y] == 0: # 경계선 및 벽이면 가지 않음
                maze[x][y] = 1 # 방문한 곳을 벽으로 함 (나중에 덧씌워지는 것을 방지)
                dis[x][y] = dis[temp[0]][temp[1]] + 1 # 방문한 지점에서 +1
                dq.append((x, y))
    if dis[6][6] == 0:
        print(-1)
    else:
        print(dis[6][6])