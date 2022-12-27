# 8. 사과나무 (BFS)
import sys
from collections import deque
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline
# 내 풀이
if __name__=="__main__":
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    dQ=deque()
    chk = [list([0] * N) for _ in range(N)]
    dQ.append((N//2, N//2))
    L = 0
    answer = 0
    while dQ:
        x, y = dQ.popleft()
        if x == 0:
            answer += lst[x][y]
            break
        else:
            if chk[x][y] == 0:
                chk[x][y] = 1
                answer += lst[x][y]
                dQ.append((x, y-1))
                dQ.append((x+1, y))
                dQ.append((x, y+1))
                dQ.append((x-1,y))
    print(answer)

# 강의 풀이
def a():
    # 12시 방향부터 차례로 순서 지정 (섹션2 강의 참조) 이후 for문 처리로 수행
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    # 강의에서는 x가 0에 닿았을 때가 아니라 L이 정해진 값을 초과했을 때 종료하도록 설정
    L = 0
    if L == N //2:
        return