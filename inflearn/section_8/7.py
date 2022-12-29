# 7. 알리바바와 40인의 도둑 (Bottom-Up)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    # lst = []
    # dy = []
    # for _ in range(N):
    #     lst.append(list(map(int,input().split())))
    #     dy.append([0] * N)
    # 또는 이렇게 할 수 있다.
    lst = [list(map(int,input().split())) for _ in range(N)]
    dy = [[0] * N for _ in range(N)]
    dy[0][0] = lst[0][0]
    for i in range(1, N):
        dy[0][i] = dy[0][i-1] + lst[0][i]
        dy[i][0] = dy[i-1][0] + lst[i][0]
    for n in range(1, N):
        for m in range(1, N):
            upper = dy[n-1][m]
            left = dy[n][m-1]
            dy[n][m] = min(upper, left) + lst[n][m]
    print(dy[N-1][N-1])