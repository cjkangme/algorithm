import sys
from collections import deque
sys.stdin=open("inflearn/section_5/input.txt", "r")

must = input().strip()
N = int(input())
for n in range(1, N+1):
    que = deque([c for c in must])
    string = input().strip()
    for c in string:
        if c in que:
            cls = que.popleft()
            if c == cls:
                continue
            else:
                break
    if que:
        print(f'#{n} NO')
    else:
        print(f'#{n} YES')
