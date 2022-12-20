# 1158. 요세푸스 문제

from collections import deque

N, K = map(int,input().split())
deck = deque(list(range(1,N+1)))
josepus = []
while deck:
    for _ in range(K-1):
        deck.append(deck.popleft())
    josepus.append(deck.popleft())
print(str(josepus).replace("[", "<").replace("]", ">"))