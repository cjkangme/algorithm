#25305. 커트라인

import sys
input = sys.stdin.readline

N, k = map(int,input().split())
lst = [*map(int,input().split())]
lst.sort(reverse=True)

print(lst[k-1])