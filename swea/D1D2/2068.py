# 2068. 최대수 구하기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    my_list = map(int, input().split())
    maxnum = 0
    for num in my_list:
        if maxnum < num:
            maxnum=num
        else:
            continue
    print(f'#{test_case} {maxnum}')
    # ///////////////////////////////////////////////////////////////////////////////////