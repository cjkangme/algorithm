# 9021 괄호
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    string = input().strip()
    is_VPS = "NO"
    opens = []
    for c in string:
        if c == "(":
            opens.append(c)
        else:
            if len(opens) == 0:
                break
            else:
                opens.pop()
    else:
        if len(opens) == 0:
            is_VPS = "YES"
    print(is_VPS)