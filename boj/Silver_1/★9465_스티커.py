# https://www.acmicpc.net/problem/9465
# https://velog.io/@cjkangme/BOJ-9465.-%EC%8A%A4%ED%8B%B0%EC%BB%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
input = sys.stdin.readline

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        dy = [list(map(int,input().split())) for _ in range(2)]
        for j in range(1, n):
            if j == 1:
                dy[0][1] += dy[1][0]
                dy[1][1] += dy[0][0]
            else:
                dy[0][j] += max(dy[1][j-1], dy[1][j-2])
                dy[1][j] += max(dy[0][j-1], dy[0][j-2])
        print(max(dy[0][-1], dy[1][-1]))