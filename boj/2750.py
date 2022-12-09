#2750. 수 정렬하기

import sys
input = sys.stdin.readline

lst = []

T = int(input())
for _ in range(T):
    lst.append(int(input()))

def merge_sort(lst):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low,mid,high)
    def merge(low, mid, high):
        temp = []
        l, h = low, mid
        while l < mid and h < high:
            if lst[l] < lst[h]:
                temp.append(lst[l])
                l += 1
            else:
                temp.append(lst[h])
                h += 1
        while l < mid:
            temp.append(lst[l])
            l += 1
        while h < high:
            temp.append(lst[h])
            h += 1
        for i in range(low, high):
            lst[i] = temp[i - low]
    sort(0, len(lst))

merge_sort(lst)
for i in range(len(lst)):
    print(lst[i])