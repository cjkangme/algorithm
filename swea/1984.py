#1984. 중간 평균값 구하기

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1984.txt", "r")

import math

test_case = int(input())

for T in range(1, test_case + 1):
    numbers = [*map(int, input().split())]
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))

    sum = 0
    for n in numbers:
        sum += n
    avr = sum / len(numbers)
    
    if int(avr) % 2 == 1:
        avr = round(avr)
    elif int(avr) % 2 == 0 and (avr - int(avr)) >= 0.5:
        avr = math.ceil(avr)
    else:
        avr = round(avr)
    print(f'#{T} {avr}')
