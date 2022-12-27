# 1. 네트워크 선 자르기 (Bottom-Up)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    dy = [0] * (N+1)
    dy[1] = 1
    dy[2] = 2
    for i in range(3, N+1):
        dy[i] = dy[i-2] + dy[i-1]
    print(dy[N])