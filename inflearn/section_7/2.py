# 2. 휴가

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(day, profit):
    global res
    if day == N+1:
        if profit > res:
            res = profit
        return
    else:
        if day+T[day] <= N+1:
            DFS(day+T[day],profit+P[day])
        DFS(day+1, profit)



if __name__=="__main__":
    N = int(input())
    T, P = [0], [0]
    res = -1
    for _ in range(N):
        t, p = map(int,input().split())
        T.append(t)
        P.append(p)
    DFS(1,0)
    print(res)
