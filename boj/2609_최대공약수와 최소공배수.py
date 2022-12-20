A, B = map(int,input().split())
answer = 1
while True:
    chk = min(A,B)
    if chk == 1:
        break
    for n in range(2, chk+1):
        if A%n == 0 and B%n == 0:
            answer *= n
            A = A//n
            B = B//n
            break
    else:
        break
print(answer)
print(answer * A * B)