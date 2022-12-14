# 10. 최소 힙

import sys
import heapq as hq
sys.stdin=open("inflearn/section_5/input.txt", "r")

a=[]
while True:
    num = int(input())
    if num == -1:
        break
    if num == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, num)