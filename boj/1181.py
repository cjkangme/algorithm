# 1181. 단어 정렬
import sys
input = sys.stdin.readline

N = int(input())
lst = list(range(N))
for i in range(N):
    lst[i] = input()
set_lst = set(lst)
new_lst = list(set_lst)
sorted_lst = sorted(new_lst, key=lambda x:(len(x), x))

for i in range(len(sorted_lst)):
    print(sorted_lst[i], end="")