# 3.뮤직비디오 (결정알고리즘)
import sys
sys.stdin=open("inflearn/section_4/input.txt", "r")

def Count(capacity):
    cnt = 1
    sum_num = 0
    for x in live_lst:
        if sum_num + x > capacity:
            sum_num = x
            cnt += 1
        else:
            sum_num += x
    return cnt

N ,M = map(int,input().split())
live_lst = [*map(int, input().split())]

lt = max(live_lst)
rt = sum(live_lst)
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = Count(mid)
    if cnt > M:
        lt = mid + 1
    else:
        ans = mid
        rt = mid - 1

print(ans)
