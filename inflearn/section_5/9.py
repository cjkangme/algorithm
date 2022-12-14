# 9. 아나그램 (딕셔너리 해쉬)
import sys
sys.stdin=open("inflearn/section_5/input.txt", "r")

# 내 풀이
# dic_1 = {}
# dic_2 = {}
# str_1 = input()
# for c in str_1:
#     if c in dic_1:
#         dic_1[c] += 1
#     else:
#         dic_1[c] = 1
# str_2 = input()
# for c in str_2:
#     if c in dic_2:
#         dic_2[c] += 1
#     else:
#         dic_2[c] = 1
# lst_1 = sorted(dic_1.items())
# lst_2 = sorted(dic_2.items())
# if lst_1 == lst_2:
#     print("YES")
# else:
#     print("NO")

# 강의 풀이 반영
# dic_1 = {}
# dic_2 = {}
# str_1 = input()
# for c in str_1:
#     dic_1[c] = dic_1.get(c, 0) + 1 # c가 없다면 0을 return하여 1을 더한 값 저장, 있으면 value를 가져와서 더한 값 저장
# str_2 = input()
# for c in str_2:
#     dic_2[c] = dic_2.get(c, 0) + 1
# for key, value in dic_1.items():
#     if key in dic_2.keys():
#         if value == dic_2[key]:
#             continue
#         else:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")

# 개선 코드
dic = {}
str_1 = input()
str_2 = input()
for c in str_1:
    dic[c] = dic.get(c, 0) + 1 # c가 없다면 0을 return하여 1을 더한 값 저장, 있으면 value를 가져와서 더한 값 저장
for c in str_2:
    dic[c] = dic.get(c, 0) - 1
for key, value in dic.items():
    if value != 0:
        print("NO")
        break
else:
    print("YES")