# 1918. 후위 표기식
import sys
input = sys.stdin.readline

def Operator(c):
    if c == "+" or c =="-":
        while stack:
            if stack[-1] == "(":
                stack.pop()
                break
            res.append(stack.pop())
        stack.append(c)
    elif c == "*" or c == "/":
        while stack:
            if stack[-1] == "*" or stack[-1] == "/":
                res.append(stack.pop())
            else:
                if stack[-1] == "(":
                    stack.pop()
                break
        stack.append(c)
    else:
        Operator(stack.pop(c))
        

math = input().rstrip()
res = []
stack = []
for c in math:
    if "A" <= c <= "Z":
        res.append(c)
    else:
        if not stack:
            stack.append(c)
        elif c == "(":
            stack.append(c)
        elif c == ")":
            Operator("+")
            stack.pop()
        else:
            Operator(c)
while stack:
    res.append(stack.pop())
print(''.join(res))