# 3. 양팔저울(DFS)

import sys
sys.stdin=open("inflearn/section_7/input.txt", "r")
input = sys.stdin.readline

#내 풀이는 리스트 이용
# 강의 풀이는 set 자료구조 이용 -> 가볍다
def DFS(L, weight):
    if L == N: # 어짜피 최종적으로 잰 무게게 잴 수 있는 무게므로 매 순서마다 추가하지 않아도 된다.
        if 0<weight<=S:
            X.add(weight) # set은 중복을 허용하지 않기 때문에 따로 중복체크를 하지 않아도 됌(시간복잡도 절약), append가 아니라 add를 사용
        return
    else:
        DFS(L+1,weight+A[L])
        DFS(L+1,weight)
        DFS(L+1, weight-A[L])

if __name__=="__main__":
    N = int(input())
    A = [*map(int,input().split())]
    S = sum(A)
    X = set()
    DFS(0, 0)
    print(S-len(X))
