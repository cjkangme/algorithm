#1934. 최소 공배수

import math
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    print(math.lcm(A,B))