# 17298. 오큰수
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
stack = [0] #인덱스 역할을 하는 스택
res = [-1] * N #오큰수가 없으면 -1을 출력하지 않으므로 우선 전부 -1인 배열을 만듬
for i in range(1, N):
    while stack and lst[stack[-1]] < lst[i]: #스택에 저장된 인덱스와 i번째 리스트를 비교함
        res[stack.pop()] = lst[i] #lst[i]가 크다면 lst[스택에 저장된 인덱스]의 오큰수가 lst[i] 이므로 res에 저장하고 stack에서 인덱스를 뺌
    stack.append(i) #답을 구하지 못하더라도 인덱스를 스택에 저장해야 나중에 더 큰 수가 나왔을 때 처리 가능
print(*res)