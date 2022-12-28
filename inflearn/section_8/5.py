# 5. 최대 선 연결하기 (최대 증가 수열 응용)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    lst = list(map(int,input().split()))
    dy_u = [1] * N
    for i in range(1, N):
        for j in reversed(range(i)):
            if lst[i] > lst[j] and dy_u[j] >= dy_u[i]:
                dy_u[i] = dy_u[j] + 1

    print(max(dy_u))