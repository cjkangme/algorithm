# https://www.acmicpc.net/problem/11052

import sys
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    lst = list(map(int,input().split()))
    lst.insert(0,0)
    dy = [0] * (N+1)
    dy[1] = lst[1]
    for i in range(2,N+1):
        max_num = 0
        for j in reversed(range(i)):
            temp = dy[j] + lst[i-j]
            if temp > max_num:
                max_num = temp
        dy[i] = max_num
    print(dy[N])