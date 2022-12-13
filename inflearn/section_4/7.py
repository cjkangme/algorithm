import sys
sys.stdin=open("inflearn/section_4/input.txt", "r")

# 내 풀이 (좀 비효율적 인듯)
# L = int(input())
# height = [*map(int,input().split())]
# M = int(input())
# for _ in range(M):
#     max_num = max(height)
#     max_idx = height.index(max_num)
#     min_num = min(height)
#     min_idx = height.index(min_num)
#     height[max_idx] -= 1
#     height[min_idx] += 1
# max_num = max(height)
# min_num = min(height)
# print(max_num - min_num)

# 강의 접근
L = int(input())
height = [*map(int,input().split())]
M = int(input())
for _ in range(M):
    height.sort()
    height[0] += 1
    height[-1] -= 1
height.sort()
print(height[-1] - height[0])