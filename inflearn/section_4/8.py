import sys
from collections import deque
sys.stdin=open("inflearn/section_4/input.txt", "r")

N, M = map(int,input().split())
lst = [*map(int,input().split())]
lst.sort()
deq = deque(lst)
cnt = 0
while deq:
    if len(deq) == 1:
        cnt += 1
        break
    if deq[0] + deq[-1] > M:
        cnt += 1
        deq.pop()
    else:
        deq.popleft() #deque에서 쓸 수 있는 O(1)의 가장 첫번째 자료를 꺼내는 방법
        deq.pop()
        cnt += 1
print(cnt)
