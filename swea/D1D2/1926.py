# 1926. 간단한 369게임(D2)

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1926.txt", "r")

T = int(input())

for number in range(1, T+1):
    flag = 0
    for string in str(number):
        if string == '3' or string == '6' or string =='9':
            print('-', end='')
            flag = 1

    if flag == 0:
        print(number, end='')
    flag = 0
    print('', end=' ')