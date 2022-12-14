# 5. 공주 구하기
import sys
from collections import deque
sys.stdin=open("inflearn/section_5/input.txt", "r")

N, K = map(int,(input().split()))
que = deque(range(1, N+1))
for _ in range(N-1):
    for _ in range(K-1):
        que.append(que.popleft())
    que.popleft()
print(que.pop())
