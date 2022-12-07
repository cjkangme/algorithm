def devide(num):
    if num % 2 == 0: #짝수일 경우
        max_num = num // 2
        for n in range(2, max_num + 1):
            if num % n == 0:
                return num//n, n
        else:
            return num, 0
    else: #홀수일 경우
        max_num = num // 3
        for n in range(2, max_num + 1):
            if num % n == 0:
                return num//n, n
        else:
            return num, 0

N = int(input())
if N == 1:
    pass
else:
    arr = []
    while N != 1:
        N, argu = devide(N)
        if argu == 0:
            arr.append(N)
            break
        arr.append(argu)
    arr.sort()
    for i in range(len(arr)):
        print(arr[i])
    