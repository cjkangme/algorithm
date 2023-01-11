# https://www.acmicpc.net/problem/15990

import sys
input = sys.stdin.readline

if __name__=="__main__":
    T = int(input())
    lst = tuple(int(input()) for _ in range(T))
    max_num = max(lst)
    dy = [[0 for _ in range(3)] for _ in range(max_num+1)] # 이렇게 해야 list의 요소를 하나씩 바꿀 수 있다.
    dy[1] = [1,0,0]
    dy[2] = [0,1,0]
    dy[3] = [1,1,1]
    devider = 1000000009
    for i in range(4, max_num+1):
        dy[i][0] = dy[i-1][1]%devider + dy[i-1][2]%devider # devider로 나누지 않으면 수가 너무 커져서 연산시간이 오래 걸린다.
        dy[i][1] = dy[i-2][0]%devider + dy[i-2][2]%devider
        dy[i][2] = dy[i-3][0]%devider + dy[i-3][1]%devider
    for num in lst:
        print(sum(dy[num]) % devider) 