# 8. 뒤집은 소수

import sys
import math
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

def reverse(x):
    string = str(x)
    string_rev = reversed(string)
    return int(''.join(string_rev))

def isPrime(x):
    if x == 1:
        return False
    max_num = math.isqrt(x)
    for n in range(2, max_num + 1):
        if x % n == 0:
            return False
    return True



N = int(input())
lst = list(map(int,input().split()))
for x in lst:
    x_rev = reverse(x)
    if isPrime(x_rev):
        print(x_rev, end=" ")