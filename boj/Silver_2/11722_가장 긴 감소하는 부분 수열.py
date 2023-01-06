# https://www.acmicpc.net/problem/11722

import sys
input = sys.stdin.readline

def dynamic(i):
    temp = [dy[idx] for idx in range(i) if A[idx] > A[i]]
    if temp:
        dy[i] = max(temp) + 1
    else:
        dy[i] = 1

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    dy = [0] * N
    for i in range(N):
        dynamic(i)
    print(max(dy))