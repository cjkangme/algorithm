import sys
sys.stdin=open("inflearn/section_5/input.txt", "r")

N = int(input())
dic = {}
for _ in range(N):
    dic[input()] = 1
for _ in range(N-1):
    dic[input()] -= 1
for key, value in dic.items():
    if value == 1:
        print(key)
