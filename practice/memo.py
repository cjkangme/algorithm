import sys
input = sys.stdin.readline

T = int(input())
cnt = 0
for t in range(T):
    string = input()
    chr_list = []
    i = 0
    is_group = True
    for c in string:
        if c not in chr_list:
            chr_list.append(c)
        else:
            if string[i-1] == c:
                pass
            else:
                is_group = False
        i += 1
    if is_group:
        cnt += 1
print(cnt)