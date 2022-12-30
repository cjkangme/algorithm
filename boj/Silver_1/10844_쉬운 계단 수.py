# https://www.acmicpc.net/problem/10844

if __name__=="__main__":
    N = int(input())
    devider = 1000000000
    dy = [[1 for _ in range(10)] for _ in range(2)]
    dy[0][0] = 0
    for _ in range(N-1):
        for i in range(10):
            if i == 0:
                dy[1][i] = dy[0][i+1]%devider
            elif i == 9:
                dy[1][i] = dy[0][i-1]%devider
            else:
                dy[1][i] = dy[0][i-1]%devider + dy[0][i+1]%devider
        for j in range(10):
            dy[0][j] = dy[1][j]
    print(sum(dy[0])%devider)