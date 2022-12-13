# 9093. 단어 뒤집기
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    string = [*map(str,input().split())]
    for s in string:
        print(s[::-1], end=" ")
    print()