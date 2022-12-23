# 7. 소수의 개수 (에라토스테네스 체)

import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

N = int(input())
prime_list = [True] * (N+1)
cnt = 0

for n in range(2, N+1):
    if prime_list[n]:
        cnt += 1
        for i in range(n+n, N+1, n):
            prime_list[i] = False

print(cnt)