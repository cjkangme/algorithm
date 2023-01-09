# 사다리 타기 (DFS)
import sys
sys.stdin = open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline


def DFS(L, x):
    chk[L][x] = 1
    if L == 0:
        print(x)
        return
    else:
        if 0 <= x+1 < 10 and board[L][x+1] == 1 and chk[L][x+1] == 0:
            DFS(L, x+1)
        elif 0 <= x-1 < 10 and board[L][x-1] == 1 and chk[L][x-1] == 0:
            DFS(L, x-1)
        else:
            DFS(L-1, x)


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    for i in range(10):
        chk = [[0] * 10 for _ in range(10)]
        if board[9][i] == 2:
            DFS(9, i)
