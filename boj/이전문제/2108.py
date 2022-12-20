#2108. 통계학
import sys
input = sys.stdin.readline

N = int(input())
lst = list(range(N))
cnt_lst = [0] * 8001 # -4000 ~ 4000
for i in range(N):
    lst[i] = int(input())
    cnt_lst[lst[i] + 4000] += 1

lst.sort()

#산술평균
avg = sum(lst) / N
if avg < 0.5 and avg > -0.5:
    avg = 0
elif abs(avg) - int(abs(avg)) < 0.5:
    avg = int(avg)
else:
    if avg < 0:
        avg = int(avg) + 1
    else:
        avg = int(avg) - 1
print(avg)

#중앙값
print(lst[N//2])
#최빈값
cnt_mode = max(cnt_lst) 
if cnt_lst.count(cnt_mode) == 1:
    print(cnt_lst.index(cnt_mode) - 4000)
else:
    index = cnt_lst.index(cnt_mode)
    print(cnt_lst.index(cnt_mode, index+1) - 4000)
#범위
print(max(lst)-min(lst))