##1859. 백만 장자 프로젝트
import sys
sys.stdin = open("D:\coding\\algorithm\swea\\1859.txt", "r")

def find_max_price(price):
    try: max_price = max(price)
    except: max_price = 1000001
    finally: return max_price

test_case = int(input())
for case in range(test_case):
    day = int(input())
    price = [*map(int, input().split())]
    count = 0
    profit = 0
    max_price = 0
    for i in range(day):
        today_price = price[i]
        if max_price == 0:
            max_price = find_max_price(price[i+1:])
            if today_price < max_price:
                profit -= today_price
                count += 1
        elif today_price < max_price:
            profit -= today_price
            count += 1
        else:
            if count > 0:
                profit += today_price * count
                count = 0
                max_price = find_max_price(price[i+1:])
            else:
                max_price = find_max_price(price[i+1:])
    print(f'#{case+1} {profit}')