# 4. 돌다리 건너기 (Bottom-Up)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    dy = [0] * (N+2)
    dy[1] = 1
    dy[2] = 2
    for i in range(3, N+2):
        dy[i] = dy[i-1] + dy[i-2]
    print(dy[N+1]) # 돌 개수 N개 + 마지막 도착지점 1개