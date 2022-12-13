#4. 후위식 연산
import sys
sys.stdin=open("inflearn/section_5/input.txt", "r")

string = input()
stack = []

for c in string:
    if c.isdecimal():
        stack.append(int(c))
    else:
        if c == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif c == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif c == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif c == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b//a)
print(stack.pop())