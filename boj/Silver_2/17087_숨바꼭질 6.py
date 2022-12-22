# https://www.acmicpc.net/problem/17087

import sys
input = sys.stdin.readline

def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a

if __name__=="__main__":
    N, S = map(int,input().split())
    a=[*map(int,input().split())]
    ans = 0
    for idx, value in enumerate(a):
        a[idx] = abs(S - value)
    if S != 1:
        for _ in range(N-1):
            a.append(gcd(a.pop(), a.pop()))
    print(a.pop())