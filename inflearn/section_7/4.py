# 4. 동전 바꿔주기

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(L, sum):
    global cnt
    if L == k:
        if sum == T:
            cnt += 1
        return
    elif sum > T:
        return
    else:
        for n in range(coins[L][1]+1):
            DFS(L+1, sum+coins[L][0]*n)

if __name__=="__main__":
    T = int(input())
    k = int(input())
    coins = list(range(k))
    for i in range(k):
        coins[i] = [*map(int,input().split())]
    cnt = 0
    DFS(0,0)
    print(cnt)