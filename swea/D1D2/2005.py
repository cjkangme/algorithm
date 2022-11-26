#2005. 파스칼의 삼각형 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\2005.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    print(f'#{test_case}')
    N = int(input())
    prev_lst = list()
    curr_lst = list()
    for i in range(1, N+1):
        if N <= 2:
            for j in range(i):
                print(1, end=' ')
            prev_lst = [1, 1]
        else:
            curr_lst = [1] * (len(prev_lst) + 1)
            for j in range(1, len(prev_lst)):
                curr_lst[j] = prev_lst[j-1] + prev_lst[j]
            for tree in curr_lst:
                print(tree, end=' ')
            prev_lst = curr_lst
        print()
        