# 홀수만 더하기
'''
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   
'''


T = int(input())
for test_case in range(1, T + 1):
    my_list = map(int, input().split())
    sum = 0
    for num in my_list:
        if num % 2 == 1:
            sum += num
    print(f'#{test_case} {sum}')