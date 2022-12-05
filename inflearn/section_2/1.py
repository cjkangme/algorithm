import sys
sys.stdin=open("input.txt", "r")

p, K = map(int, input().split())

cnt = 0

for x in range(1, p+1):
    if p % x == 0:
        cnt += 1
    if cnt == K:
        print(x)
        break
else:
    print(-1)