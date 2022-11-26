# 2056. 연월일 달력

from datetime import datetime
import sys
sys.stdin = open("D:\coding\\algorithm\swea\\2056.txt", "r")

T = int(input())
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T+1):
    test_list = str(input())
    year = test_list[0:4]
    month = test_list[4:6]
    day = test_list[6:8]
    today = f'{year}/{month}/{day}'
    if 0 < int(month) < 13 and 0 < int(day) <= days.get(int(month)):
        print(f'#{test_case} {today}')
    else:
        print(f'#{test_case} {-1}')

'''
for test_case in range(1, T+1):
    test_list = input()
    year = test_list[0:4]
    month = test_list[4:6]
    day = test_list[6:8]
    today = f'{year}/{month}/{day}'
    try:
        datetime.strptime(today, '%Y/%m/%d')
        print(f'#{test_case} {today}')
    except:
        print(f'#{test_case} {-1}')
'''
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
   case = str(input())
   year = case[0:4]
   month = case[4:6]
   day = case[6:8]
   
   answer = ''
   if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
       answer = year + '/' + month + '/' + day
   else:
       answer += '-1'
​
   print("#" + str(test_case) + " " + answer)
'''