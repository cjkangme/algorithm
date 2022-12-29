# 9. 가방문제(냅색 알고리즘)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

# if __name__ == "__main__":
#     n, limit = map(int,input().split())
#     lst = []
#     for _ in range(n):
#         lst.append(tuple(map(int,input().split())))
#     dy = [0] * (limit+1)
#     for i in range(1, limit+1):
#         for weight, value in lst:
#             if i >= weight:
#                 temp = dy[i-weight] + value
#                 if temp > dy[i]:
#                     dy[i] = temp
#     print(dy[limit])

# 또 다른 풀이
if __name__ == "__main__":
    n, limit = map(int,input().split())
    lst = []
    for _ in range(n):
        lst.append(tuple(map(int,input().split())))
    dy = [0] * (limit+1)
    for weight, value in lst:
        for i in range(weight, limit+1):
            dy[i] = max(dy[i-weight] + value, dy[i])
    print(dy[limit])