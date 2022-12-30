# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    A = list(map(int,input().split()))
    dy = [0 for _ in range(N)]
    dy[0] = 1
    for i in range(1, N):
        for j in reversed(range(i)):
            if A[i] > A[j] and dy[i] <= dy[j]:
                dy[i] = dy[j] + 1
        if dy[i] == 0:
            dy[i] = 1
    print(max(dy))