# 10. 조합 구하기
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline
# 내 풀이
def DFS(L, n):
    global cnt
    if L == M:
        print(*res)
        cnt += 1
        return
    else:
        for i in range(1,N+1):
            if chk[i] == 0 and i > n: ## <<< i > n 이 조합을 나누는 데 중요함
                chk[i] = 1
                res.append(i)
                DFS(L+1, i)
                chk[i] = 0
                res.pop()

#강의 풀이
def DFS_2(L, S):
    global cnt
    if L == M:
        print(*res)
        cnt += 1
        return
    else:
        for i in range(S,N+1): # 인자를 range의 시작점부터 도는 것으로 함 (이전 값의 +1부터 시작하니 무조건 큰 수)
            if chk[i] == 0:
                chk[i] = 1
                res.append(i)
                DFS_2(L+1, i+1)
                chk[i] = 0
                res.pop()

if __name__=="__main__":
    N, M = map(int,input().split())
    cnt = 0
    chk = [0] * (N+1)
    res = []
    DFS_2(0, 1)
    print(cnt)
