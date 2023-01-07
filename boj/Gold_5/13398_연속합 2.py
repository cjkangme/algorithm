# https://www.acmicpc.net/problem/13398

import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    A = list(map(int, input().split()))
    dy = [[-1001] * 2 for _ in range(n)]
    dy[0][0] = A[0]
    if n > 1:
        dy[1][0] = max(dy[0][0] + A[1], A[1])
        dy[1][1] = A[1]
    for i in range(2, n):
        dy[i][0] = max(dy[i-1][0]+A[i], A[i])
        dy[i][1] = max(dy[i-1][1]+A[i], dy[i-2][0]+A[i])
    answer = -1001
    for n1, n2 in dy:
        answer = max(answer, n1, n2)
    print(answer)