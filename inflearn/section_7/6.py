# 6. 알파코드

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

def DFS(L, P):
    global cnt
    if L == length:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+ord("A")-1), end="")
        print()
        return
    else:
        for i in range(1, 10):
            if code[L] == i:
                res[P] = i
                DFS(L+1, P+1)
        for i in range(10, 27):
            if code[L] == i//10 and code[L+1] == i%10:
                res[P] = i
                DFS(L+2, P+1)
                

if __name__=="__main__":
    code = list(map(int,input()))
    length = len(code)
    code.append(-1)
    cnt = 0
    res = [0] * (length+3)
    DFS(0, 0)
    print(cnt)
    