# https://www.acmicpc.net/problem/11057

if __name__=="__main__":
    N = int(input())
    dy = [[1 for _ in range(10)] for _ in range(N)]
    for i in range(1, N):
        for j in range(1, 10):
            dy[i][j] = (dy[i-1][j] + dy[i][j-1]) % 10007
    print(sum(dy[-1]) % 10007)