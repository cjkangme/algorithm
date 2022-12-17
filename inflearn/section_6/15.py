# 15. 경로 탐색(그래프 DFS)

import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

def DFS(n):
    global cnt
    if n == N:
        cnt += 1
        return
    else:
        for i in range(1, N+1):
            if A[n][i] == 1 and chk[i] == 0:
                chk[i] = 1
                DFS(i)
                chk[i] = 0

if __name__=="__main__":
    N, M = map(int,input().split())
    A = [[0] * (N+1) for _ in range(N+1)]
    chk = [0] * (N+1)
    chk[1] = 1
    cnt = 0
    for _ in range(M):
        i, j = map(int,input().split())
        A[i][j] = 1
    DFS(1)
    print(cnt)