N = int(input())
cnt = 0
numbers = list(range(1, N+1))
for num in numbers:
    str_num = str(num)
    if len(str_num) <= 2:
        cnt += 1
        continue
    gap = int(str_num[1]) - int(str_num[0])
    flag = False
    for i in range(1, len(str_num)-1):
        flag = True
        if int(str_num[i+1]) - int(str_num[i]) != gap:
            flag = False
            break
    if flag == True:
        cnt += 1
print(cnt)