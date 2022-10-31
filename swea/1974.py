# 1974. 스도쿠 검증 D2

import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1974.txt", "r")

test_case = int(input())

for T in range(1, test_case + 1):
    sudoku = []
    flag = 0
    for _ in range(9):
        sudoku.append([*map(int, input().split())])
    
    # 가로 검증
    for i in range(len(sudoku)):
        result = []
        for num in sudoku[i]:
            if num not in result:
                result.append(num)
        # 중복값이 제거되여 result 배열 길이가 다르다면 0 출력
        if len(result) != len(sudoku):
            flag += 1
            break
    if flag >= 1:
        print(f'#{T} 0')
        continue
    
    # 3 X 3 검증
    for start_row in range(0, len(sudoku),3):
        for start_col in range(0, len(sudoku),3):
            result = []
            for i in range(start_row,start_row+3):
                for j in range(start_col, start_col+3):
                    if sudoku[i][j] not in result:
                        result.append(sudoku[i][j])
            if len(result) != len(sudoku):
                flag += 1
    if flag >= 1:
        print(f'#{T} 0')
        continue
    
    # 세로 검증
    for i in range(len(sudoku)):
        result = []
        for j in range(len(sudoku)):
            num = sudoku[j][i]
            if num not in result:
                result.append(num)
    # 중복값이 제거되여 result 배열 길이가 다르다면 0 출력
        if len(result) != len(sudoku):
            flag += 1
            break
    if flag == 0:
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')


