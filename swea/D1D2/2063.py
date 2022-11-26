# 2063. 중간값 찾기
import sys
sys.stdin = open("D:\coding\\algorithm\swea\\2063.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    my_list = [*map(int, input().split())]
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i] > my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
            else:
                continue
    print(my_list[int((i+1)/2)])
    break

'''
my_list = [*map(int, input().split())]
my_list.sort()
n = T // 2
print(my_list.sort(n))
'''