import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L == m:
        for num in range(L):
            print(lst[num], end=" ")
        print()
        cnt+=1
        return
    else:
        for i in range(1, n+1):
            if chk[i] == 0:
                lst[L] = i
                chk[i] = 1
                DFS(L+1)
                chk[i] = 0 # 매우 중요!!! 호출 후 선언하는 것은 back하고 되돌아온 상황이므로, 무언가를 원상태로 돌려야할 떄는 여기에 선언해야 한다.

if __name__=="__main__":
    n, m = map(int,input().split())
    lst = list(range(m))
    chk = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)