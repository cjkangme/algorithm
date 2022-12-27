# 2. 네트워크 선 자르기 (Top-down)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

def DFS(L):
    if L == 1 or L == 2:
        return L
    elif dy[L]:
        return dy[L]
    else:
        dy[L] = DFS(L-1) + DFS(L-2)
        return dy[L]

if __name__=="__main__":
    N = int(input())
    dy = [0] * (N+1)
    print(DFS(N))