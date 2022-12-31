# https://www.acmicpc.net/problem/14002

import sys
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    A = list(map(int,input().split()))
    d = [0 for _ in range(N)]
    idx = [A[0]]
    d[0] = 1
    for i in range(1,N):
        for j in reversed(range(i)):
            if A[i] > A[j] and d[i] <= d[j]:
                d[i] = d[j] + 1
        if d[i] == 0:
            d[i] = 1
    max_d = max(d)
    max_idx = d.index(max_d)
    LIS = [A[max_idx]]
    for k in reversed(range(max_idx)):
        if d[k] == max_d-1 and A[k] < LIS[-1]:
            max_d -= 1
            LIS.append(A[k])
    print(max(d))
    print(*reversed(LIS))