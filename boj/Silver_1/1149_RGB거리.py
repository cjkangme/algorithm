# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    house = [tuple(map(int,input().split())) for _ in range(N)]
    dy = [[0 for _ in range(3)] for _ in range(N)]
    for i in range(N):
        R, G, B = house[i]
        if i == 0:
            dy[i][0] = R
            dy[i][1] = G
            dy[i][2] = B
        else:
            dy[i][0] = min(dy[i-1][1], dy[i-1][2]) + R
            dy[i][1] = min(dy[i-1][0], dy[i-1][2]) + G
            dy[i][2] = min(dy[i-1][0], dy[i-1][1]) + B
    print(min(dy[-1]))