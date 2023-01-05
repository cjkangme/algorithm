# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    dy = [0] * n
    dy[0] = int(input())
    for length in range(2, n+1):
        lst = list(map(int, input().split()))
        temp = dy.copy() # 이렇게 안하면 temp와 lst는 같은 객체를 지정하는 말이 된다.
        for i, value in enumerate(lst):
            if i == 0:
                dy[i] = temp[i] + value
            elif i == length - 1:
                dy[i] = temp[i-1] + value
            else:
                dy[i] = max(temp[i], temp[i-1]) + value
    print(max(dy))
                