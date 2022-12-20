#10814. 나이순 정렬
import sys
input = sys.stdin.readline

N = int(input())
lst = list(range(N))
for i in range(N):
    lst[i] = [*map(str, input().split())]
    lst[i][0] = int(lst[i][0])
sorted_lst = sorted(lst, key=lambda x : x[0])

for i in range(N):
    print(f'{sorted_lst[i][0]} {sorted_lst[i][1]}')