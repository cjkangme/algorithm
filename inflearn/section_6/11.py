# 11. 수들의 조합
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

def DFS(L, S, sum):
    global cnt
    if L == K:
        if sum % M == 0:
            cnt+=1
        return
    else:
        for i in range(S, N):
            if chk[i] == 0:
                chk[i] = 1
                DFS(L+1, i+1, sum+A[i])
                chk[i] = 0


if __name__=="__main__":
    N, K = map(int,input().split())
    A = [*map(int,input().split())]
    M = int(input())

    cnt = 0
    chk = [0] * N

    DFS(0,0,0)
    print(cnt)