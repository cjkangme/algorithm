#10828. 스택
import sys
input = sys.stdin.readline

def process(command, stack, num):
    def push(stack, num):
        stack.append(num)
    def pop(stack):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    def size(stack):
        print(len(stack))
    def empty(stack):
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    def top(stack):
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    if command == "push":
        push(stack, num)
    elif command == "pop":
        pop(stack)
    elif command == "size":
        size(stack)
    elif command == "empty":
        empty(stack)
    elif command == "top":
        top(stack)
    return stack

N = int(input())
stack = []
for _ in range(N):
    command = input().strip()
    if command[0:4] == "push":
        command, num = command.split()
    else:
        num = 0
    stack = process(command, stack, int(num))