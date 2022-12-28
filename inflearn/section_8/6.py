# 6. 가장 높은 탑 쌓기 (LIS 응용)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline         

if __name__=="__main__":
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(tuple(map(int,input().split())))
    lst.sort(key=lambda x: x[0], reverse=True)
    dy = [0] * N
    for i in range(N):
        dy[i] = lst[i][1]
        max_height = 0
        for j in reversed(range(i)):
            if lst[j][2] > lst[i][2] and dy[j] > max_height:
                max_height = dy[j]
        dy[i] += max_height
    print(max(dy))