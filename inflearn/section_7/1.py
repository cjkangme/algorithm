# 1. 최대 점수 구하기

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(n, score, time):
    global max_score
    if time > M:
        return
    elif n == N:
        if score > max_score:
            max_score = score
        return
    else:
        # 풀었냐 안풀었냐 두가지면 됨
        DFS(n+1, score+A[n], time+B[n])
        DFS(n+1, score, time)

if __name__=="__main__":
    N,M = map(int,input().split())
    A = []
    B = []
    max_score = -1
    for _ in range(N):
        score, time = map(int,input().split())
        A.append(score)
        B.append(time)
    DFS(0,0,0)
    print(max_score)