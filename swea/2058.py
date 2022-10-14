# 2058. 자릿수 더하기

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\2058.txt", "r")

n = int(input())
a = n // 1000 # 6
b = n // 100 - a * 10
c = n // 10 - a * 100 - b * 10
d = n % 10

print(a + b + c + d)