import sys
from collections import deque
sys.stdin=open("inflearn/section_5/input.txt", "r")

N, M = map(int,input().split())
lst = [(pos, val) for pos, val in enumerate(list(map(int,input().split())))]
que = deque(lst)
cnt = 0
while que:
    max_que = max(que, key=lambda x: x[1])
    max_danger = max_que[1]
    patient = que.popleft()
    if patient[1] == max_danger:
        cnt += 1
        if patient[0] == M:
            break
    else:
        que.append(patient)
print(cnt)