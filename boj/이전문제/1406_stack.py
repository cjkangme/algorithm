# 1406. 에디터
import sys
input = sys.stdin.readline


stack_left = list(input().strip())
stack_right = []
M = int(input())


for _ in range(M):
    command = input().strip()
    if command[0] == "P":
        command, c = command.split()
        stack_left.append(c)
    elif command == "L":
        if len(stack_left) > 0:
            stack_right.append(stack_left.pop())
    elif command == "D":
        if len(stack_right) > 0:
            stack_left.append(stack_right.pop())
    else:
        if len(stack_left) > 0:
            stack_left.pop()
            
stack_right.reverse()
stack_left.extend(stack_right)
print("".join(stack_left))