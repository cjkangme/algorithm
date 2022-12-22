# https://www.acmicpc.net/problem/9613

import sys
input = sys.stdin.readline

def gcd(n1,n2):
    res = 1
    while n1 > 1 and n2 > 1:
        max_num = min(n1, n2)
        for m in range(2, max_num+1):
            if n1 % m == 0 and n2 % m == 0:
                n1 = n1 // m
                n2 = n2 // m
                res *= m
                break
        else: break
    return res
                

if __name__=="__main__":
    n = int(input())
    for _ in range(n):
        ans = 0
        a = [*map(int,input().split())]
        for i in range(1,a[0]):
            for j in range(i+1,a[0]+1):
                ans += gcd(a[i], a[j])
        print(ans)