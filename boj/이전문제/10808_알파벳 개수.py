# 10808. 알파벳 개수

import sys
input = sys.stdin.readline

S = input().rstrip()
res = [0] * 26
for c in S:
    res[ord(c)-ord("a")] += 1
print(*res)