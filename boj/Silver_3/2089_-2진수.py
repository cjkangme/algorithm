# https://www.acmicpc.net/problem/2089

import sys

def DFS(L, sum):
    global answer
    if L < 0:
        if sum == N:
            while answer[-1] == 0:
                answer.pop()
            while answer:
                print(answer.pop(), end="")
            sys.exit(0)
        return
    elif abs(sum - N) > abs(b_list[L+1]) and abs(sum + N) > abs(b_list[L+1]):
        return
    else:
        answer[L] = 1
        DFS(L-1, sum+b_list[L])
        answer[L] = 0
        DFS(L-1, sum)

if __name__=="__main__":
    N = int(input())
    max_L = 0

    max_num = 2000000000 * 16
    b_num = 1
    b_list = []
    while max_num > 0:
        b_list.append(b_num)
        b_num *= -2
        max_num = max_num // 2

    temp = abs(N)
    while temp > 0:
        temp //= 4
        max_L += 1
    max_L = max_L * 2 + 1
    answer = [0] * (max_L + 1)
    if N == 0:
        print(0)
    else:
        DFS(max_L, 0)