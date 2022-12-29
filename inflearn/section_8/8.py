# 8. 알리바바와 40인의 도둑 (Bottom-Up)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

def DFS(x, y):
    if x==0 and y==0:
        return lst[0][0]
    elif dy[x][y]:
        return dy[x][y]
    else:
        if y == 0:
            dy[x][y] = DFS(x-1,y) + lst[x][y]
        elif x == 0:
            dy[x][y] = DFS(x, y-1) + lst[x][y]
        else: 
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + lst[x][y]
        return dy[x][y]

if __name__=="__main__":
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    dy = [[0] * N for _ in range(N)]
    print(DFS(N-1, N-1))