# https://www.acmicpc.net/problem/1699

import math

if __name__=="__main__":
    N = int(input())
    dy = [2147000000] * (N+1)
    dy[0] = 0
    for i in range(1, N+1):
        max_num = math.isqrt(i)
        for j in range(1, max_num+1):
            dy[i] = min(dy[i], dy[i-(j**2)]+1)
    print(dy[N])