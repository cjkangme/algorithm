# 2. 랜선 자르기
import sys
sys.stdin=open("inflearn/section_4/input.txt", "r")

N, K = map(int,input().split())
lst = list(range(N))
for i in range(N):
    lst[i] = int(input())
left = 0
right = max(lst)
ans = 0
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for length in lst:
        cnt += length // mid
    if cnt < K:
        right = mid-1
    else:
        ans = mid
        left = mid+1
print(ans)