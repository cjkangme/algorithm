# 3. 부분집합 구하기 (DFS)
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")

def DFS(x):
    if x > N:
        for i in range(1, N+1):
            if chk[i] == 1:
                print(i, end=" ")
        if 1 in chk:
            print()
        return
    else:
        chk[x] = 1
        DFS(x+1)
        chk[x] = 0
        DFS(x+1)

if __name__=="__main__":
    N = int(input())
    chk=[0] * (N+1)
    DFS(1)