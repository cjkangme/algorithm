# https://www.acmicpc.net/problem/1912

import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    A = list(map(int,input().split()))
    dy = [0 for _ in range(n)]
    dy[0] = A[0]
    for i in range(1, n):
        dy[i] = max(dy[i-1]+A[i], A[i])
    print(max(dy))