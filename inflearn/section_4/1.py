# 1. 이분 검색
import sys
sys.stdin=open("inflearn/section_4/input.txt", "r")

#직접 구현
def binary_search(lst, value):
    def search(left, right):
        if left == right:
            return left + 1
        mid = (left + right) // 2
        if lst[mid] == value:
            return mid + 1
        if lst[mid] > value:
            return search(left, mid-1)
        else:
            return search(mid+1,right)
    print(search(0, len(lst)-1)) 

# 강의 구현
def binary(lst, value):
    lt, rt = 0, len(lst)-1
    while lt<=rt:
        mid = (lt+rt)//2
        if lst[mid] == value:
            print(mid+1) 
            break
        elif lst[mid] > value:
            rt = mid-1
        else:
            lt = mid+1

N, M = map(int,input().split())
lst = [*map(int,input().split())]
lst.sort()

binary_search(lst, M)
binary(lst, M)
