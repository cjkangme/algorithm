def open(i):
    global cnt
    if chk[i] == 1:
        return
    else:
        cnt+=1
        chk[i] = 1
        open(cards[i])

def solution(cards):
    cards.insert(0,0)
    N = len(cards)
    chk = [0] * N
    res1 = [] * (N-1)
    cnt = 0
    answer = 0
    for i in range(1, N+1):
        open(i)
        res1[i] = cnt
        cnt = 0
        for j in range(1, N+1):
            if chk[j] == 1:
                continue
            else:
                open(j)
                temp = res1[i] * cnt
                if temp > answer:
                    answer = temp
            
    return answer