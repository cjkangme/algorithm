# https://www.acmicpc.net/problem/1676

import math

N = int(input())
string = str(math.factorial(N))

cnt = 0
for c in string[::-1]:
    if c == "0":
        cnt += 1
    else:
        break
print(cnt)