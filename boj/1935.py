# 1935. 후위 표기식2
import sys
input = sys.stdin.readline

N = int(input())
math = input().rstrip()
A = list(range(N))
for i in range(N):
    A[i] = int(input())
    
stack = []

def calculate(c, right, left):
    if c == "+":
        stack.append(left+right)
    elif c == "-":
        stack.append(left-right)
    elif c == "*":
        stack.append(left*right)
    else:
        stack.append(left/right)

for c in math:
    if c.isupper():
        stack.append(A[ord(c)-65])
    else:
        calculate(c, stack.pop(), stack.pop())
print(f'{stack[0]:.2f}')