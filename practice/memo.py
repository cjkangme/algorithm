import sys
input = sys.stdin.readline

prime_lst = []

for num in range(2, 10001):
    sqrt = int(num ** (1/2))
    for n in range(2, sqrt + 1):
        if num % n == 0:
            break
    else:
        prime_lst.append(num)

T = int(input())
for _ in range(T):
    n = int(input())
    min_lst = []
    max_lst = []
    for i in prime_lst:
        if i > n / 2:
            break
        remain = n - i
        if remain in prime_lst:
            min_lst.append(i)
            max_lst.append(remain)
            continue
    min_num = max(min_lst)
    max_num = min(max_lst)
    print(f'{min_num} {max_num}')