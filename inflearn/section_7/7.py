# 7. 송아지 찾기 (BFS)
import sys
from collections import deque
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    S, E = map(int,input().split())
    MAX = 10000
    dis = [0] * (MAX+1)
    chk = [0] * (MAX+1)
    chk[S] = 1
    dq = deque()
    dq.append(S)
    L = 0
    while dq:
        now=dq.popleft()
        if now == E:
            break
        for next in(now+5, now+1, now-1):
            if 0 < next <= MAX and next < E+5:
                if chk[next] == 0:
                    dq.append(next)
                    chk[next] = 1
                    dis[next] = dis[now] + 1
    print(dis[E])
