# 6. 중복 순열 구하기
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

def DFS(L):
    if L == M:
        for num in ans:
            print(num, end=" ")
        print()
        return
    else:
        for i in range(1, N+1):
            ans[L] = i
            DFS(L+1)

if __name__=="__main__":
    N, M = map(int, input().split())
    ans = list(range(M))
    DFS(0)
