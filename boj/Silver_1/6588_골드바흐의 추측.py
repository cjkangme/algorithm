# https://www.acmicpc.net/problem/6588

import math
import sys
input = sys.stdin.readline

def get_prime():
    for num in range(2, 1001):
        for i in range(2, math.isqrt(num)+1):
            if num % i == 0: 
                prime_list[num] = False
                break
            

if __name__=="__main__":
    MAX_NUM = 1000000
    prime_list = [True] * (MAX_NUM+1)
    get_prime()
    for i in range(2, 1001):
        if prime_list[i]:
            for j in range(i+i, MAX_NUM+1, i):
                prime_list[j] = False
    while True:
        n = int(input())
        if n == 0: 
            break
        for a in range(2, (n//2)+1):
            b = n - a
            if prime_list[a] and prime_list[b]:
                print(f'{n} = {a} + {b}')
                break
        else:
            print("Goldbach's conjecture is wrong.")