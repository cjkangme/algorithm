# 17. 피자 배달 거리 (DFS 활용)

import sys
sys.stdin = open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

house = []
pizza = []
dfs_list = []
answer = []


def solution(lst):
    min_length = 0
    for x, y in house:
        temp = 2147000000
        for xx, yy in lst:
            temp = min(temp, abs(x-xx)+abs(y-yy))
        min_length += temp
    return min_length


def DFS(L, s):
    if L == M:
        answer.append(solution(dfs_list))
    else:
        for k in range(s, pizza_len):
            dfs_list.append(pizza[k])
            DFS(L+1, k+1)
            dfs_list.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                house.append((i, j))
            elif board[i][j] == 2:
                pizza.append((i, j))
    pizza_len = len(pizza)
    DFS(0, 0)
    print(min(answer))
