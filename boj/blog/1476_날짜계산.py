# https://www.acmicpc.net/problem/1476

if __name__ == "__main__":
    E, S, M = map(int, input().split())
    max_num = 2147000000
    for i in range(1, max_num):
        if (i-E) % 15 == 0 and (i-S) % 28 == 0 and (i-M) % 19 == 0:
            print(i)
            break
