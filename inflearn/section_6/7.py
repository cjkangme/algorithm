# 7. 동전교환
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

def DFS(L, sum):
    global res
    if L == res:
        return
    elif sum == change:
        if L < res:
            res = L
        return
    elif sum > change:
        return
    else:
        for i in range(n):
            DFS(L+1, sum+coin[i])

if __name__=="__main__":
    n = int(input())
    coin = [*map(int,input().split())]
    coin.reverse() # 초반에 가장 빠른 최소값을 찾기 위해 큰값부터 적용하도록 정렬함
    change = int(input())
    res = 501
    DFS(0, 0)
    print(res)