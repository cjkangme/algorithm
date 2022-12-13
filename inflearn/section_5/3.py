import sys
sys.stdin=open("inflearn/section_5/input.txt", "r")


string = input()
ans = ""
stack = []
for c in string:
    if c.isdecimal():
        ans += c
    else:
        if c == "(":
            stack.append(c)
        elif c == "*" or c == "/":
            while stack:
                if stack[-1] == "*" or stack[-1] == "/":
                    ans += stack.pop()
                else:
                    stack.append(c)
                    break
            else:
                stack.append(c)
        elif c == "+" or c== "-":
            while stack:
                if stack[-1] != "(":
                    ans += stack.pop()
                else:
                    stack.append(c)
                    break
            else:
                stack.append(c)
        elif c == ")":
            while stack[-1] != "(":
                ans += stack.pop()
            stack.pop() # 남은 괄호 제거

        
while stack:
    ans += stack.pop()

print(ans)
