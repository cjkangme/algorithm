# 1. 재귀함수를 이용한 이진수 출력

import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")

# 내 풀이
def binary(num, i):
    power = 2**i
    if num > power:
        num = binary(num, i+1)
    else:
        return num
    if num >= power:
        num -= power
        print(1, end="")
    else:
        print(0, end="")
    return num

# 강의 풀이
def DFS(x):
    if x == 0:
        return #함수 종료
    else:
        DFS(x//2) # ex) 11의 경우 5로 DFS 재귀
        print(x%2, end='') # ex) 11의 경우 1 출력
    

if __name__ == "__main__":
    num = int(input())
    binary(num, 0)
    print()
    DFS(num)