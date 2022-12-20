# 11650. 좌표 정렬하기
import sys
input = sys.stdin.readline

N = int(input())
lst = list(range(N))
for i in range(N):
    lst[i] = [*map(int,input().split())]
# lst[i][0] (x좌표) 기준으로 오름차순 정렬 후, lst[i][1] (y좌표) 기준으로 오름차순 정렬
sorted_lst = sorted(lst, key=lambda x: (x[0], x[1]))

for coordinate in sorted_lst:
    print(f'{coordinate[0]} {coordinate[1]}')