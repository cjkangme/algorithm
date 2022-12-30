# 10. 동전교환 (냅색 알고리즘)

import sys
sys.stdin=open("inflearn/section_8/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N = int(input())
    coins = list(map(int,input().split()))
    change = int(input())
    dy = [2147000000 for _ in range(change+1)]
    dy[0] = 0
    for coin in coins:
        for i in range(coin, change+1):
            dy[i] = min(dy[i-coin] + 1, dy[i])
    print(dy[change])