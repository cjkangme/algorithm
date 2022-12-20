import sys
input = sys.stdin.readline

lst = list(range(9))
max_value = -1
N = 0
M = 0
for i in range(9):
    lst[i] = [*map(int,input().split())]
    max_num = max(lst[i])
    if max_value < max_num:
        max_value = max_num
        N = i
        M = lst[i].index(max_value)
print(max_value)
print(f'{N+1} {M+1}')