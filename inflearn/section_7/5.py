# 5. 동전분해하기

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(L):
    global answer
    if L == N:
        if people[0] != people[1] and people[1] != people[2] and people[0] != people[2]:
            diff = max(people) - min(people)
            if diff < answer:
                answer = diff
        return
    else:
        for j in range(3):
            people[j] += coins[L]
            DFS(L+1)
            people[j] -= coins[L]

if __name__=="__main__":
    N = int(input())
    people = [0] * 3
    coins = [0] * N
    for i in range(N):
        coins[i] = int(input())
    answer = 2147000000
    DFS(0)
    print(answer)