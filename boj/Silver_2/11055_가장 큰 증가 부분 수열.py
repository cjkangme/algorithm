# https://www.acmicpc.net/problem/11055

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split()))
    dy = A.copy()
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                dy[i] = max(dy[j]+A[i], dy[i])
    print(max(dy))