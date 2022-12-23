# K번째 큰 수 구하기

import sys
sys.stdin=open("inflearn/section_2/input.txt", "r")
input = sys.stdin.readline

N, K = map(int,input().split())
lst = [*map(int,input().split())]
lst.sort(reverse=True)
ans = set()

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum_num = lst[i] + lst[j] + lst[k]
            ans.add(sum_num)
tup = sorted(ans, reverse=True) # set은 index가 없으므로 sorted를 통해 튜플로 반환받아야 한다.
print(tup[K-1])
