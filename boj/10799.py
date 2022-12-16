# 10799. 쇠막대기
import sys
input = sys.stdin.readline

q = input().rstrip()
stack = []
cnt = 0

for i, c in enumerate(q):
    if c == "(":
        stack.append(c)
    else:
        if q[i-1] == "(":
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)