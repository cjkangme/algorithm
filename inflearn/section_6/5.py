# 5. 바둑이 승차 (DFS)
import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")

# 내 풀이
def DFS(L, sum, t_sum):
    global result
    if sum > C:
        return
    elif sum + (total - t_sum) < result: #남은 것을 다 더해도 현재 결과보다 작을 경우 더 계산할 필요가 없다.
        return
    elif L == N:
        if sum > result:
            result = sum
        return
    else:
        DFS(L+1, sum+lst[L], sum+lst[L])
        DFS(L+1, sum, sum+lst[L])


if __name__=="__main__":
    C, N = map(int,input().split())
    lst = list(range(N))
    result = -1
    for i in range(N):
        lst[i] = int(input())
    lst.sort()
    total = sum(lst)
    DFS(0,0,0)
    print(result)
