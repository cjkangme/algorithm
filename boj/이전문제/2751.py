#2751. 수 정렬하기
import sys
input = sys.stdin.readline

def merge_sort(lst):
    def sort(left, right):
        if right - left < 2:
            return
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)
    def merge(left, mid, right):
        temp = []
        l, h = left, mid
        while l < mid and h < right:
            if lst[l] > lst[h]:
                temp.append(lst[h])
                h += 1
            else:
                temp.append(lst[l])
                l += 1
        while l < mid:
            temp.append(lst[l])
            l += 1
        while h < right:
            temp.append(lst[h])
            h += 1
        for i in range(left, right):
            lst[i] = temp[i - left]
    sort(0, len(lst))
            
T = int(input())
lst = list(range(T))
for i in range(T):
    lst[i] = int(input())

merge_sort(lst)
for num in lst:
    print(num)