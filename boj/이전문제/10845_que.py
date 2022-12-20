# 10845. 큐
import sys
from collections import deque
input = sys.stdin.readline

def command(com):
    if com == "pop":
        if que:
            return que.popleft()
        else:
            return -1
    
    elif com == "size":
        return len(que)
    
    elif com == "empty":
        if que:
            return 0
        else:
            return 1
    
    elif com == "front":
        if que:
            return que[0]
        else:
            return -1
    
    elif com == "back":
        if que:
            return que[-1]
        else:
            return -1
    
    else:
        com, num = com.split()
        que.append(int(num))
        return False

N = int(input())
que = deque()

for _ in range(N):
    res = command(input().rstrip())
    if res:
        print(res)