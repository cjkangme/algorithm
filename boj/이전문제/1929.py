# 1929. 소수 구하기
M, N = map(int,input().split())
prime_arr = []
def get_prime(num):
    sqrt = int(num ** (1 / 2))
    for n in range(2, sqrt + 1):
        if num % n == 0:
            return False
    else:
        return True

for num in range(M, N+1):
    if num == 1:
        continue
    if get_prime(num):
        print(num)
        prime_arr.append(num)