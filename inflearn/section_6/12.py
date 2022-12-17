# 12. 라이브러리를 이용한 순열
import sys
import itertools as it
sys.stdin=open("inflearn/section_6/input.txt", "r")
input = sys.stdin.readline

if __name__=="__main__":
    N, target = map(int,input().split())
    b = [1] * N
    for i in range(1,N):
        b[i] = b[i-1] * (N-i) // i
    a = list(range(1, N+1))
    for tmp in it.permutations(a):
        sum = 0
        for i, n in enumerate(tmp):
            sum+=n * b[i]
        if sum == target:
            print(*tmp)
            break