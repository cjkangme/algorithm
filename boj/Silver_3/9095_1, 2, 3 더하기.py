# https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

def DFS(sum_num):
    global cnt
    if sum_num > n:
        return
    elif sum_num == n:
        cnt += 1
        return
    else:
        DFS(sum_num+1)
        DFS(sum_num+2)
        DFS(sum_num+3)

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        cnt = 0
        DFS(0)
        print(cnt)