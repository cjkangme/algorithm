import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1859.txt", "r")

test_case = int(input())
for case in range(test_case):
    day = int(input())
    price = [*map(int, input().split())]

    max_price = price[-1]
    profit = 0

    for i in range(day-2, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            profit += max_price - price[i]
    print(f'#{case+1} {profit}')