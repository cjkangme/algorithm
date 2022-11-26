# 2070. 큰 놈, 작은 놈, 같은 놈

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    left, right = map(int, input().split())
    if left < right:
        print(f'#{test_case} <')
    elif left > right:
        print(f'#{test_case} >')
    else:
        print(f'#{test_case} =')
    # ///////////////////////////////////////////////////////////////////////////////////