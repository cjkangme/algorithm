#18870. 좌표 압축
import sys
input = sys.stdin.readline

N = int(input())
lst = [*map(int, input().split())]
sorted_set = set(lst)
sorted_lst = list(sorted_set)
sorted_lst.sort()

dic = {}
for i in range(len(sorted_lst)):
    dic[sorted_lst[i]] = i  
for num in lst:
    print(dic[num], end=" ")