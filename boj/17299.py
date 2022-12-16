# 오등큰수
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
F = [0] * (max(A)+1)
res = [-1] * (N)
stack = [0]

for i in A:
    F[i] += 1

for i in range(1,N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        res[stack.pop()] = A[i]
    stack.append(i)
    
print(*res)