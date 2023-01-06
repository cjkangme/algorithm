# https://www.acmicpc.net/problem/11054

import sys
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    A = list(map(int,input().split()))
    dy = [[0] * 2 for _ in range(N)]
    max_dy = 0
    for i in range(N):
        temp1 = [dy[idx][0] for idx in range(i) if A[idx] < A[i]]
        if temp1:
            dy[i][0] = max(temp1) + 1
        else:
            dy[i][0] = 1
    for j in reversed(range(N)):
        temp2 = [dy[idx][1] for idx in range(j+1, N) if A[idx] < A[j]]
        if temp2:
            dy[j][1] = max(temp2) + 1
        else:
            dy[j][1] = 0
    for x, y in dy:
        max_dy = max(max_dy, x+y)
    print(max_dy)