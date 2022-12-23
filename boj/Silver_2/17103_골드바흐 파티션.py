# https://www.acmicpc.net/problem/17103

import sys
import math
input = sys.stdin.readline

if __name__=="__main__":
    MAX_NUM = 1000000
    prime_list = [True] * (MAX_NUM + 1)
    for i in range(2, math.isqrt(MAX_NUM) + 1):
        if prime_list[i] == True:
            for j in range(i+i, MAX_NUM+1, i):
                prime_list[j] = False
    T = int(input())
    for _ in range(T):
        N = int(input())
        cnt = 0
        for num in range(2, N//2+1):
            if prime_list[num]:
                remain = N - num
                if prime_list[remain]:
                    cnt += 1
        print(cnt)