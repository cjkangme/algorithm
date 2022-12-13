import sys
sys.stdin=open("inflearn/section_5/input.txt", "r")

string = input()
stack = []
cnt = 0
for i in range(len(string)):
    if string[i] == "(":
        stack.append(string[i])
    else:
        if string[i-1] == "(":
            stack.pop() #레이저이므로 쇠막대기 길이에 포함되지 않음
            cnt+=len(stack)
        else:
            stack.pop() #쇠막대기가 끝남
            cnt+=1 #마지막으로 잘리고 남은 조각
print(cnt)
