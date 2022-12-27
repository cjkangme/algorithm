# 3. 계단 오르기 (Top-down)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

def DFS(L):
    if dy[L]:
        return dy[L]
    else:
        dy[L] = DFS(L-1) + DFS(L-2)
        return dy[L]

if __name__=="__main__":
    N = int(input())
    dy = [0] * (N+1)
    dy[1] = 1
    dy[2] = 2
    print(DFS(N))
    