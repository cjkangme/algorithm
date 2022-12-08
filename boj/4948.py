#4948. 베르트랑 공준
import sys
import math
input = sys.stdin.readline

def get_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True

prime_arr = []
max_num = 123456 * 2
for num in range(2, max_num):
    if get_prime(num):
        prime_arr.append(num)

while True:
    num = int(input())
    
    if num == 0:
        break
        
    cnt = 0
    
    if num == 1:
        print(1)
        continue
        
    for n in prime_arr:
        if n > num and n <= num * 2:
            cnt += 1
        
    print(cnt)