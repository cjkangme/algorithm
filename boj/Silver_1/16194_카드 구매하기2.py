# https://www.acmicpc.net/problem/16194

import sys
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    P = list(map(int,input().split()))
    P.insert(0,0)
    dy = [2147000000] * (N+1)
    dy[0] = 0
    for i in range(1, N+1):
        for j in reversed(range(i)):
            temp = dy[j] + P[i-j]
            if temp < dy[i]:
                dy[i] = temp
    print(dy[N])