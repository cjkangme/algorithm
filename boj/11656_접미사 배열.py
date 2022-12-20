string = input()
ans_list = []
for i in range(len(string)):
    ans_list.append(string[i:])
ans_list.sort()
for answer in ans_list:
    print(answer)