# https://www.acmicpc.net/problem/2225

if __name__=="__main__":
    N, K = map(int,input().split())
    dy = [0] * (N+1)
    dy[0] = 1
    co = [[x for _ in range(N)] for x in range(K)]
    for i in range(1, K):
        for j in range(1, N):
            co[i][j] = co[i-1][j] + co[i][j-1]
    for k in range(1, N+1):
        dy[k] = dy[k-1] + co[K-1][k-1]
    print(dy[N]%1000000000)