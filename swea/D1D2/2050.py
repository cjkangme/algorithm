#2050. 알파벳을 숫자로 변환

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\2050.txt", "r")

case = input()
for alphabet in case:
    number = ord(alphabet) - 64
    print(number, end = ' ')