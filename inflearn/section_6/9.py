import sys
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

#내 풀이
def Combination(n, r):
    upper = 1
    lower = 1
    for i in range(r):
        upper *= n-i
        lower *= r-i
    return (upper // lower)

def DFS(L):
    global res
    if L == N:
        if res == target:
            print(*lst)
            sys.exit(0)
        return
    elif res > target:
        return
    else:
        for i in range(1, N+1):
            if chk[i] == 0:
                chk[i] = 1
                lst.append(i)
                res += i * b[L]
                DFS(L+1)
                chk[i] = 0
                lst.pop()
                res -= i * b[L]


if __name__=="__main__":
    N, target = map(int,input().split())
    res = 0 #함수의 인자로 넣어도 된다.
    lst = []
    chk = [0] * (N+1)
    b = [1] * N
    # 더 간단히 하는 방법
    for i in range(1, N):
        b[i]=b[i-1] * (N-i) / i
    DFS(0)